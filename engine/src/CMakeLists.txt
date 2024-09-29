include_directories(${CMAKE_CURRENT_SOURCE_DIR})
add_executable(${PROJECT_NAME}
        main.cc
        media/ffmpeg_audio_decoder.cc
        media/ffmpeg_audio_decoder.h
        media/ffmpeg_demux_decoder.cc
        media/ffmpeg_demux_decoder.h
        media/ffmpeg_video_decoder.cc
        media/ffmpeg_video_decoder.h
)

target_link_libraries(${PROJECT_NAME}
        ffmpeg::avcodec
        ffmpeg::avformat
        ffmpeg::swresample
        stb::stb
)
