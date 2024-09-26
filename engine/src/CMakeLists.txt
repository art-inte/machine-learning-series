include_directories(${CMAKE_CURRENT_SOURCE_DIR})
add_executable(${PROJECT_NAME}
        main.cc
)

target_link_libraries(${PROJECT_NAME}
        ffmpeg::avcodec
        ffmpeg::avformat
        ffmpeg::swresample
)
