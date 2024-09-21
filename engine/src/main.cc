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

int main(const int argc, char* argv[]) {
    if (argc < 2) {
        return EXIT_FAILURE;
    }
    const char* output_filename = argv[1];
    AVFormatContext* output_format_context;
    AVCodecContext* video_codec_context = nullptr;
    const AVCodec* video_codec = nullptr;
    AVStream* video_stream = nullptr;
    bool have_video = false;
    AVCodecContext* audio_codec_context = nullptr;
    const AVCodec* audio_codec = nullptr;
    AVStream* audio_stream = nullptr;
    bool have_audio = false;

    // Allocate the output media context.
    avformat_alloc_output_context2(&output_format_context, nullptr, nullptr, output_filename);
    if (!output_format_context) {
        printf("Could not deduce output format from file extension: using MPEG.\n");
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
        have_video = true;
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
        audio_stream->time_base = {1, audio_codec_context->sample_rate };
        if (output_format_context->oformat->flags & AVFMT_GLOBALHEADER) {
            audio_codec_context->flags |= AV_CODEC_FLAG_GLOBAL_HEADER;
        }
        have_audio = true;
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

    return EXIT_SUCCESS;
}
