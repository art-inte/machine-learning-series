#ifndef RENDERER_FFMPEG_VIDEO_DECODER_H
#define RENDERER_FFMPEG_VIDEO_DECODER_H

extern "C" {
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
}

namespace media {
    class FFmpegVideoDecoder {
    public:
        bool Init(const char* file_path);

        void Reset();
    private:
        bool OpenCodecContext(enum AVMediaType type);

        AVFormatContext* format_context_ = nullptr;
        AVCodecContext* decoder_context_ = nullptr;
        int stream_index_ = -1;
        AVPacket* packet_ = nullptr;
        AVFrame* frame_ = nullptr;
    };
}

#endif //RENDERER_FFMPEG_VIDEO_DECODER_H
