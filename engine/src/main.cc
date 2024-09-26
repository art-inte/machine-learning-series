#include <cstdlib>

extern "C" {
#include <libavformat/avformat.h>
#include <libavcodec/avcodec.h>
#include <libswresample/swresample.h>
#include <libavutil/timestamp.h>
}

constexpr int WIDTH = 3840;
constexpr int HEIGHT = 2160;
constexpr int FRAME_RATE = 30;
constexpr AVPixelFormat PIXEL_FORMAT = AV_PIX_FMT_YUV420P;
constexpr int DURATION = 10;
constexpr int BIT_RATE = 256000;
constexpr int SAMPLE_RATE = 48000;

static bool WriteFrame(AVFormatContext* format_context, AVCodecContext* codec_context,
                       const AVStream* stream, const AVFrame* frame, AVPacket* packet) {
    if (packet == nullptr) {
        return false;
    }
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
        AVRational* time_base = &format_context->streams[packet->stream_index]->time_base;
        av_log(nullptr, AV_LOG_INFO, "pts: %s pts_time: %s duration: %s duration_time: %s stream_index:%d\n",
               av_ts2str(packet->pts), av_ts2timestr(packet->pts, time_base),
               av_ts2str(packet->duration), av_ts2timestr(packet->duration, time_base),
               packet->stream_index);
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

static AVFrame* GetAudioFrame(const AVCodecContext* codec_context, AVFrame* temp_frame,
                              int64_t& next_pts, float& t, float& cr, float& cr2) {
    if (temp_frame == nullptr) {
        return nullptr;
    }
    auto* q = (int16_t*) temp_frame->data[0];

    if (av_compare_ts(next_pts, codec_context->time_base, DURATION, {1, 1}) > 0) {
        return nullptr;
    }

    for (int j = 0; j < temp_frame->nb_samples; j++) {
        auto v = (int16_t)(sinf(t) * 10000);
        for (int i = 0; i < codec_context->ch_layout.nb_channels; i++) {
            *q++ = v;
        }
        t += cr;
        cr += cr2;
    }

    temp_frame->pts = next_pts;
    next_pts += temp_frame->nb_samples;
    return temp_frame;
}

// Encode one audio frame and send it to the muxer.
// Return true when encoding is finished, false otherwise.
static bool WriteAudioFrame(AVFormatContext* format_context, AVCodecContext* codec_context,
                            SwrContext* swr_context, const AVStream* stream, AVPacket* packet,
                            AVFrame* frame, AVFrame* temp_frame,
                            int64_t& next_pts, int64_t& sample_count, float& t, float& cr, float& cr2) {
    if (frame == nullptr) {
        return false;
    }
    temp_frame = GetAudioFrame(codec_context, temp_frame, next_pts, t, cr, cr2);
    if (temp_frame) {
        auto dst_nb_samples = swr_get_delay(swr_context, codec_context->sample_rate) + temp_frame->nb_samples;
        if (av_frame_make_writable(temp_frame)) {
            return false;
        }
        if (swr_convert(swr_context, frame->data, int(dst_nb_samples),
                        (const uint8_t**) temp_frame->data, frame->nb_samples) < 0) {
            return false;
        }
        frame->pts = av_rescale_q(sample_count, {1, codec_context->sample_rate}, codec_context->time_base);
        sample_count += dst_nb_samples;
    } else {
        return true;
    }
    return WriteFrame(format_context, codec_context, stream, frame, packet);
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
    SwrContext* swr_context = nullptr;
    AVStream* audio_stream = nullptr;
    AVPacket* audio_packet = nullptr;
    AVFrame* audio_frame = nullptr;
    AVFrame* audio_temp_frame = nullptr;
    int64_t next_audio_pts = 0;
    int64_t sample_count = 0;
    float t = 0, cr, cr2;
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
            return EXIT_FAILURE;
        }
        audio_stream->id = static_cast<int>(output_format_context->nb_streams) - 1;
        audio_codec = avcodec_find_encoder(output_format_context->oformat->audio_codec);
        if (!audio_codec) {
            return EXIT_FAILURE;
        }
        audio_codec_context = avcodec_alloc_context3(audio_codec);
        if (!audio_codec_context) {
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
        audio_stream->time_base = { 1, audio_codec_context->sample_rate };
        if (output_format_context->oformat->flags & AVFMT_GLOBALHEADER) {
            audio_codec_context->flags |= AV_CODEC_FLAG_GLOBAL_HEADER;
        }
        if (swr_alloc_set_opts2(&swr_context,
                            &audio_codec_context->ch_layout,
                            audio_codec_context->sample_fmt,
                            audio_codec_context->sample_rate,
                            &audio_codec_context->ch_layout,
                            AV_SAMPLE_FMT_S16,
                            audio_codec_context->sample_rate,
                            0,
                            nullptr) < 0) {
            return EXIT_FAILURE;
        }
        if (swr_init(swr_context) < 0) {
            swr_free(&swr_context);
            return EXIT_FAILURE;
        }
        audio_packet = av_packet_alloc();
        if (!audio_packet) {
            av_packet_free(&audio_packet);
            return EXIT_FAILURE;
        }
        audio_frame = av_frame_alloc();
        if (!audio_frame) {
            av_frame_free(&audio_frame);
            return EXIT_FAILURE;
        }
        audio_frame->format = audio_codec_context->sample_fmt;
        audio_frame->ch_layout = audio_codec_context->ch_layout;
        audio_frame->sample_rate = audio_codec_context->sample_rate;
        audio_frame->nb_samples = 1024;
        if (av_frame_get_buffer(audio_frame, 0) < 0) {
            av_log(nullptr, AV_LOG_ERROR, "Error allocating an audio buffer\n");
            return EXIT_FAILURE;
        }
        audio_temp_frame = av_frame_alloc();
        if (!audio_temp_frame) {
            av_frame_free(&audio_temp_frame);
            return EXIT_FAILURE;
        }
        audio_temp_frame->format = AV_SAMPLE_FMT_S16;
        audio_temp_frame->ch_layout = audio_codec_context->ch_layout;
        audio_temp_frame->sample_rate = audio_codec_context->sample_rate;
        audio_temp_frame->nb_samples = 1024;
        if (av_frame_get_buffer(audio_temp_frame, 0) < 0) {
            return EXIT_FAILURE;
        }
        cr = float(2 * M_PI * 110.0 / audio_codec_context->sample_rate);
        cr2 = float(2 * M_PI * 110.0 / audio_codec_context->sample_rate / audio_codec_context->sample_rate);
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

    while (encode_video || encode_audio) {
        if (video_codec_context == nullptr || audio_codec_context == nullptr) {
            return EXIT_FAILURE;
        }
        if (encode_video &&
            (!encode_audio || av_compare_ts(next_video_pts, video_codec_context->time_base,
                next_audio_pts, audio_codec_context->time_base) <= 0)) {
            encode_video = !WriteVideoFrame(output_format_context, video_codec_context, video_stream,
                video_packet, video_frame, next_video_pts);
        } else {
            encode_audio = !WriteAudioFrame(output_format_context, audio_codec_context,
                                            swr_context, audio_stream,
                audio_packet, audio_frame, audio_temp_frame, next_audio_pts, sample_count, t, cr, cr2);
        }
    }
    av_write_trailer(output_format_context);
    if (have_video) {
        avcodec_free_context(&video_codec_context);
        av_packet_free(&video_packet);
        av_frame_free(&video_frame);
    }
    if (have_audio) {
        avcodec_free_context(&audio_codec_context);
        swr_free(&swr_context);
        av_packet_free(&audio_packet);
        av_frame_free(&audio_frame);
        av_frame_free(&audio_temp_frame);
    }
    if (!(output_format_context->oformat->flags & AVFMT_NOFILE)) {
        avio_closep(&output_format_context->pb);
    }
    avformat_free_context(output_format_context);
    return EXIT_SUCCESS;
}
