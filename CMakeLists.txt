cmake_minimum_required(VERSION 3.15)
project(salty CXX)


add_executable(crypto src/bob.cpp)

add_library(salty src/salty.cpp)
target_include_directories(salty PUBLIC include)



set_target_properties(salty PROPERTIES PUBLIC_HEADER "include/salty.h")
install(TARGETS salty)
