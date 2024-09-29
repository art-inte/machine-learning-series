cmake_minimum_required(VERSION 3.23)
project(renderer CXX)

find_package(FFmpeg REQUIRED)
find_package(stb REQUIRED)

add_subdirectory(src/)
