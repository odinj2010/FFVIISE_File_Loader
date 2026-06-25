cmake_minimum_required(VERSION 3.12)
project(FF7DirectLoader LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Configure output directories
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Create a shared library that compiles as d3d11.dll
add_library(d3d11 SHARED
    d3d11_proxy.cpp
    d3d11_proxy.h
    hooks.cpp
    hooks.h
)

# Export definition for C-style functions
set_target_properties(d3d11 PROPERTIES 
    PREFIX ""
    SUFFIX ".dll"
)

# Link standard libraries
target_link_libraries(d3d11 PRIVATE kernel32 user32 d2d1 dwrite)

