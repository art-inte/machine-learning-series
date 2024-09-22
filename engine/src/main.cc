#include <cstdlib>

extern "C" {
#include <libavformat/avformat.h>
#include <libavcodec/avcodec.h>
}

constexpr int WIDTH = 3840;
constexpr int HEIGHT = 2160;
constexpr int FRAME_RATE = 30;
constexpr AVPixelFormat PIXEL_FORMAT = AV_PIX_FMT_YUV420P;
constexpr int DURATION = 10;
constexpr int BIT_RATE = 256000;
constexpr int SAMPLE_RATE = 48000;

static void LogPacket(const AVFormatContext* format_context, const AVPacket* packet) {
    AVRational* time_base = &format_context->streams[packet->stream_index]->time_base;

}

static bool WriteFrame(AVFormatContext* format_context, AVCodecContext* codec_context,
                       const AVStream* stream, const AVFrame* frame, AVPacket* packet) {
    // Send the frame to the encoder.
    int ret = avcodec_send_frame(codec_context, frame);
    if (ret < 0) {
        av_log(nullptr, AV_LOG_ERROR, "Error sending a frame to the encoder\n");
        return false;
    }
    while (true) {
        ret = avcodec_receive_packet(codec_context, packet);
        if (ret == AVERROR(EAGAIN) || ret == AVERROR_EOF) {
            break;
        }
        if (ret < 0) {
            av_log(nullptr, AV_LOG_ERROR, "Error encoding a frame\n");
            return false;
        }
        av_packet_rescale_ts(packet, codec_context->time_base, stream->time_base);
        packet->stream_index = stream->index;
        ret = av_interleaved_write_frame(format_context, packet);
        if (ret < 0) {
            return false;
        }
    }
    return ret == AVERROR_EOF;
}

static AVFrame* GetVideoFrame(const AVCodecContext* codec_context,
                              AVFrame* frame, int64_t& next_pts) {
    if (frame == nullptr) {
        return nullptr;
    }
    // Check if we want to generate more frames.
    if (av_compare_ts(next_pts, codec_context->time_base, DURATION,  {1, 1}) > 0) {
        return nullptr;
    }
    if (av_frame_make_writable(frame) < 0) {
        return nullptr;
    }

    const int index = static_cast<int>(next_pts);
    // Y
    for(int y = 0; y < frame->height; y++) {
        for (int x = 0; x < frame->width; x++) {
            frame->data[0][y * frame->linesize[0] + x] = x + y + index * 3;
        }
    }
    // Cb and Cr
    for (int y = 0; y < frame->height / 2; y++) {
        for (int x = 0; x < frame->width / 2; x++) {
            frame->data[1][y * frame->linesize[1] + x] = 128 + y + index * 2;
            frame->data[2][y * frame->linesize[2] + x] = 64 + y + index * 5;
        }
    }

    frame->pts = next_pts++;
    return frame;
}

// Encode one video frame and send it to the muxer.
// return true when encoding is finished, false otherwise.
static bool WriteVideoFrame(AVFormatContext* format_context, AVCodecContext* codec_context,
                            const AVStream* stream, AVPacket* packet, AVFrame* frame, int64_t& next_pts) {
    frame = GetVideoFrame(codec_context, frame, next_pts);
    return WriteFrame(format_context, codec_context, stream, frame, packet);
}

static void CloseStream(AVPacket* video_packet, AVFrame* video_frame) {
    av_packet_free(&video_packet);
    av_frame_free(&video_frame);
}

int main(const int argc, char* argv[]) {
    if (argc < 2) {
        return EXIT_FAILURE;
    }
    const char* output_filename = argv[1];
    AVFormatContext* output_format_context;
    AVCodecContext* video_codec_context = nullptr;
    const AVCodec* video_codec = nullptr;
    AVStream* video_stream = nullptr;
    AVPacket* video_packet = nullptr;
    AVFrame* video_frame = nullptr;
    int64_t next_video_pts = 0;
    bool have_video = false;
    bool encode_video = false;
    AVCodecContext* audio_codec_context = nullptr;
    const AVCodec* audio_codec = nullptr;
    AVStream* audio_stream = nullptr;
    bool have_audio = false;
    bool encode_audio = false;

    // Allocate the output media context.
    avformat_alloc_output_context2(&output_format_context, nullptr, nullptr, output_filename);
    if (!output_format_context) {
        av_log(nullptr, AV_LOG_ERROR ,
            "Could not deduce output format from file extension: using MPEG.\n");
        avformat_alloc_output_context2(&output_format_context, nullptr, "mpeg", output_filename);
    }
    if (!output_format_context) {
        return EXIT_FAILURE;
    }

    // Add the audio and video streams using the default format codecs and initialize the codecs.
    if (output_format_context->oformat->video_codec != AV_CODEC_ID_NONE) {
        video_stream = avformat_new_stream(output_format_context, nullptr);
        if (!video_stream) {
            return EXIT_FAILURE;
        }
        video_stream->id = static_cast<int>(output_format_context->nb_streams) - 1;
        video_stream->time_base = { 1, FRAME_RATE };
        video_codec = avcodec_find_encoder(output_format_context->oformat->video_codec);
        if (!video_codec) {
            return EXIT_FAILURE;
        }
        video_codec_context = avcodec_alloc_context3(video_codec);
        video_codec_context->codec_id = output_format_context->oformat->video_codec;
        video_codec_context->width = WIDTH;
        video_codec_context->height = HEIGHT;
        video_codec_context->time_base = video_stream->time_base;
        video_codec_context->gop_size = 12;
        video_codec_context->pix_fmt = PIXEL_FORMAT;
        if (video_codec_context->codec_id == AV_CODEC_ID_MPEG2VIDEO) {
            video_codec_context->max_b_frames = 2;
        }
        if (video_codec_context->codec_id == AV_CODEC_ID_MPEG1VIDEO) {
            video_codec_context->mb_decision = 2;
        }
        if (output_format_context->oformat->flags & AVFMT_GLOBALHEADER) {
            video_codec_context->flags |= AV_CODEC_FLAG_GLOBAL_HEADER;
        }
        video_packet = av_packet_alloc();
        if (!video_packet) {
            av_packet_free(&video_packet);
            return EXIT_FAILURE;
        }
        video_frame = av_frame_alloc();
        if (!video_frame) {
            av_frame_free(&video_frame);
            return EXIT_FAILURE;
        }
        video_frame->format = video_codec_context->pix_fmt;
        video_frame->width = video_codec_context->width;
        video_frame->height = video_codec_context->height;
        // Allocate the buffers for the frame data.
        if (av_frame_get_buffer(video_frame, 0) < 0) {
            av_log(nullptr, AV_LOG_ERROR, "Could not allocate video frame data\n");
            return EXIT_FAILURE;
        }
        have_video = true;
        encode_video = true;
    }
    if (output_format_context->oformat->audio_codec != AV_CODEC_ID_NONE) {
        audio_stream = avformat_new_stream(output_format_context, nullptr);
        if (!audio_stream) {
            CloseStream(video_packet, video_frame);
            return EXIT_FAILURE;
        }
        audio_stream->id = static_cast<int>(output_format_context->nb_streams) - 1;
        audio_codec = avcodec_find_encoder(output_format_context->oformat->audio_codec);
        if (!audio_codec) {
            CloseStream(video_packet, video_frame);
            return EXIT_FAILURE;
        }
        audio_codec_context = avcodec_alloc_context3(audio_codec);
        if (!audio_codec_context) {
            CloseStream(video_packet, video_frame);
            return EXIT_FAILURE;
        }
        audio_codec_context->sample_fmt = audio_codec->sample_fmts ?
            audio_codec->sample_fmts[0] : AV_SAMPLE_FMT_FLTP;
        audio_codec_context->bit_rate = BIT_RATE;
        audio_codec_context->sample_rate = SAMPLE_RATE;
        if (audio_codec->supported_samplerates) {
            audio_codec_context->sample_rate = audio_codec->supported_samplerates[0];
            for (int i = 0; audio_codec->supported_samplerates[i]; i++) {
                if (audio_codec->supported_samplerates[i] == SAMPLE_RATE) {
                    audio_codec_context->sample_rate = SAMPLE_RATE;
                }
            }
        }
        audio_codec_context->ch_layout = AV_CHANNEL_LAYOUT_STEREO;
        audio_stream->time_base = {1, audio_codec_context->sample_rate };
        if (output_format_context->oformat->flags & AVFMT_GLOBALHEADER) {
            audio_codec_context->flags |= AV_CODEC_FLAG_GLOBAL_HEADER;
        }
        have_audio = true;
        encode_audio = true;
    }

    if (have_video && video_stream) {
        if (avcodec_open2(video_codec_context, video_codec, nullptr) < 0) {
            return EXIT_FAILURE;
        }
        if (avcodec_parameters_from_context(video_stream->codecpar, video_codec_context) < 0) {
            return EXIT_FAILURE;
        }
    }
    if (have_audio && audio_stream) {
        if (avcodec_open2(audio_codec_context, audio_codec, nullptr) < 0) {
            return EXIT_FAILURE;
        }
        if (avcodec_parameters_from_context(audio_stream->codecpar, audio_codec_context) < 0) {
            return EXIT_FAILURE;
        }
    }
    av_dump_format(output_format_context, 0, output_filename, 1);

    // Open the output file, if needed.
    if (!(output_format_context->oformat->flags & AVFMT_NOFILE)) {
        if (avio_open(&output_format_context->pb, output_filename, AVIO_FLAG_WRITE) < 0) {
            av_log(nullptr, AV_LOG_ERROR, "Could not open output file: %s\n", output_filename);
            return EXIT_FAILURE;
        }
    }
    // Write the stream header, if any.
    if (avformat_write_header(output_format_context, nullptr) < 0) {
        av_log(nullptr, AV_LOG_ERROR, "Error occurred when opening output file\n");
        return EXIT_FAILURE;
    }

    while (next_video_pts < FRAME_RATE * DURATION) {
        WriteVideoFrame(output_format_context, video_codec_context, video_stream,
            video_packet, video_frame, next_video_pts);
    }

    av_write_trailer(output_format_context);

    CloseStream(video_packet, video_frame);

    return EXIT_SUCCESS;
}
