 cmake_minimum_required(VERSION 2.8.3)
project(makeathon)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  sensor_msgs
)

catkin_package()

add_executable(distancia2 src/distancia2.cpp ${RPLIDAR_SDK_SRC})
target_link_libraries(distancia2 ${catkin_LIBRARIES})

include_directories(${catkin_INCLUDE_DIRS})


