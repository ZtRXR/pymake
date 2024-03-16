# 介绍

>一个用python脚本的方式书写cmake的python库

# 如何安装

用.pth文件自行定位到本项目的文件夹中

# 如何使用
>生成一个库文件

```python
from pymake import *

(
    cmake("3.20")
    .set(cmake_export_compile_cmmands,"ON")
    .set(cmake_cxx_flags,o3)
    .set(cmake_cxx_standard,"17")
    .project(name="say_hello")
    .add_library(var(project_name),static,"main.cpp")
    .target_include_directories(var(project_name),public,"include")
    .write()
)
```

```bash
python make.py
```
将会生成CMakeLists.txt如下
```cmake
cmake_minimum_required(VERSION 3.20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_FLAGS -O3)
set(CMAKE_CXX_STANDARD 17)
project(say_hello VERSION 1.0 DESCRIPTION "a default project" LANGUAGES CXX)
add_library(${PROJECT_NAME} STATIC  main.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC  include)

```