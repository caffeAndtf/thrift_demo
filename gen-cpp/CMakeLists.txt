cmake_minimum_required(VERSION 3.0)
project(simpic)

set(CMAKE_CONFIGURATION_TYPES Release)
set(CMAKE_BUILD_TYPE Release)

add_definitions("-std=c++11")
set(PROJECT_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(CMAKE_INSTALL_PREFIX ${CMAKE_CURRENT_SOURCE_DIR}/output) # 安装路径

# opencv相关
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -O3 -Wall -g3")

set(OpenCV_DIR /Users/bytedance/apps/opencv-3.3.1/install/share/OpenCV) # 指定opencv路径

find_package(OpenCV 3.3 REQUIRED)

include_directories(/Users/bytedance/apps/opencv-3.3.1/install/include/opencv2)

message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

## 头文件设置:
include_directories(
        ${PROJECT_DIR}
        ${OpenCV_INCLUDE_DIRS}
        /usr/local/include/thrift) # 指定boost路径

aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR} source_files)
add_executable(pic_server ${source_files})
target_link_libraries(pic_server ${Opencv_LIBS} thrift opencv_dnn opencv_core opencv_highgui opencv_imgcodecs)