cmake_minimum_required(VERSION 3.23)
project(renderer CXX)

find_package(FFmpeg REQUIRED)

add_executable(${PROJECT_NAME}
        src/main.cc
)
target_link_libraries(${PROJECT_NAME}
        ffmpeg::avcodec
        ffmpeg::avformat
)
