#include "media/ffmpeg_video_decoder.h"

namespace media {
    bool FFmpegVideoDecoder::Init(const char* file_path) {
        // Open input file, and allocate format context.
        if (avformat_open_input(&format_context_, file_path, nullptr, nullptr) < 0) {
            return false;
        }
        // Retrieve stream information.
        if (avformat_find_stream_info(format_context_, nullptr) < 0) {
            return false;
        }
        if (OpenCodecContext(AVMEDIA_TYPE_VIDEO)) {
            packet_ = av_packet_alloc();
        }

        return true;
    }

    void FFmpegVideoDecoder::Reset() {
        if (frame_) {
            av_frame_free(&frame_);
            frame_ = nullptr;
        }
        if (decoder_context_) {
            avcodec_free_context(&decoder_context_);
            decoder_context_ = nullptr;
        }
        stream_index_ = -1;
    }

    bool FFmpegVideoDecoder::OpenCodecContext(enum AVMediaType type) {
        int ret = av_find_best_stream(format_context_, type, -1, -1, nullptr, 0);
        if (ret < 0) {
            return false;
        } else {
            stream_index_ = ret;
            AVStream* stream = format_context_->streams[stream_index_];
            const AVCodec* decoder = avcodec_find_decoder(stream->codecpar->codec_id);
            if (!decoder) {
                return false;
            }
            // Allocate a codec context for the decoder.
            decoder_context_ = avcodec_alloc_context3(decoder);
            if (!decoder_context_) {
                return false;
            }
            // Copy codec parameters from input stream to output codec context.
            if (avcodec_parameters_to_context(decoder_context_, stream->codecpar) < 0) {
                return false;
            }
            // Init the decoder.
            if (avcodec_open2(decoder_context_, decoder, nullptr) < 0) {
                return false;
            }
        }
        return true;
    }
}
