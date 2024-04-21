from typing import Literal, Self, Type, TypeVar
from .tools import *
from .values import *

ModesPPI = Literal["PUBLIC","PRIVATE","INTERFACE"]
ModesSSM = Literal["STATIC","SHARED","MODULE"]

class cmake:
    __write_stack__:List[str] = []
    __file_name__:str
    def __init__(self,version_min:str,file_name:str="CMakeLists.txt") -> None:
        self.__file_name__ = file_name
        self.__write_stack__.append(f"cmake_minimum_required(VERSION {version_min})")

    def write(self)->None:
        with open(file=self.__file_name__,mode="+w",encoding="utf8") as f:
            for i in self.__write_stack__:
                f.write(i)
                f.write("\n")

    def project(self,name:str="default",version:str="1.0",description:str="a default project",languages:str="CXX")->Self:
        self.__write_stack__.append(f"project({name} VERSION {version} DESCRIPTION \"{description}\" LANGUAGES {languages})")
        return self
    
    def add_executable(self,name:str=var(project_name),*source:str)->Self:
        self.__write_stack__.append(f"add_executable({name} {args_to_str(source)})")
        return self
    
    def add_library(self,name:str=var(project_name),mode:ModesSSM="STATIC",*source:str)->Self:
        """
        ARGS:
            mode: mode can be STATIC , SHARED or MODULE
        """
        self.__write_stack__.append(f"add_library({name} {mode} {args_to_str(source)})")
        return self
    
    def target_include_directories(self,for_project:str=var(project_name),mode:ModesPPI="PUBLIC",*directories:str)->Self:
        """
        ARGS:
            mode : mode can be PUBLIC PRIVATE INTERFACE
        """
        self.__write_stack__.append(f"target_include_directories({for_project} {mode} {args_to_str(directories)})")
        return self

    def set(self,name:str,value:str)->Self:
        self.__write_stack__.append(f"set({name} {value})")
        return self
    
    def target_link_libraries(self,lib_name:str,name:str=var(project_name),mode:ModesPPI="PUBLIC")->Self:
        self.__write_stack__.append(f"target_link_libraries({name} {mode} {lib_name})")
        return self
    
    def target_link_directories(self,name:str=var(project_name),mode:ModesPPI="PUBLIC",*directories:str)->Self:
        self.__write_stack__.append(f"target_link_directories({name} {mode} {args_to_str(directories)})")
        return self
    
    def just_add(self,sentence:str)->Self:
        self.__write_stack__.append(sentence)
        return self

    def file(self,new_var_name:str,mode:str=glob_recurse,*search_str:str)->Self:
        self.__write_stack__.append(f"file({mode} {new_var_name} {args_to_str(search_str)})")
        return self
    
    def add_subdirectory(self,path:str)->Self:
        self.__write_stack__.append(f"add_subdirectory({path})")
        return self