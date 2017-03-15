# Install script for directory: /home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/build/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python" TYPE FILE FILES
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/detect.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/draw_net.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/classify.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/requirements.txt"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/caffe" TYPE FILE FILES
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/classifier.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/io.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/net_spec.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/__init__.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/detector.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/pycaffe.py"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/draw.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/caffe/_caffe.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/caffe/_caffe.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/caffe/_caffe.so"
         RPATH "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/build/install/lib:/usr/local/cuda/lib64")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/caffe" TYPE SHARED_LIBRARY FILES "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/build/lib/_caffe.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/caffe/_caffe.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/caffe/_caffe.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/caffe/_caffe.so"
         OLD_RPATH "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/build/lib:/usr/local/cuda/lib64::::::::"
         NEW_RPATH "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/build/install/lib:/usr/local/cuda/lib64")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/caffe/_caffe.so")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/caffe" TYPE DIRECTORY FILES
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/imagenet"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/proto"
    "/home/student/objectDetection/faster-rcnn-resnet/caffe-fast-rcnn/python/caffe/test"
    )
endif()

