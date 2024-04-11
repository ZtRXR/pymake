from .tools import *
from .values import *

class cmake:
    __write_stack:"list[str]" = []
    __file_name = ""
    def __init__(self,version_min:"str",file_name:"str"="CMakeLists.txt") -> None:
        self.__file_name = file_name
        self.__write_stack.append(f"cmake_minimum_required(VERSION {version_min})")

    def write(self)->None:
        with open(file=self.__file_name,mode="+w",encoding="utf8") as f:
            for i in self.__write_stack:
                f.write(i)
                f.write("\n")

    def project(self,name:"str"="default",version:"str"="1.0",description:"str"="a default project",languages:"str"="CXX")->"cmake":
        self.__write_stack.append(f"project({name} VERSION {version} DESCRIPTION \"{description}\" LANGUAGES {languages})")
        return self
    
    def add_executable(self,name:"str"=var(project_name),*source:"str")->"cmake":
        self.__write_stack.append(f"add_executable({name} {args_to_str(source)})")
        return self
    
    def add_library(self,name:"str"=var(project_name),mode:"str"=static,*source:"str")->"cmake":
        """
        ARGS:
            mode: mode can be STATIC , SHARED or MODULE
        """
        self.__write_stack.append(f"add_library({name} {mode} {args_to_str(source)})")
        return self
    
    def target_include_directories(self,for_project:"str"=var(project_name),mode:"str"=public,*directories:"str")->"cmake":
        """
        ARGS:
            mode : mode can be PUBLIC PRIVATE INTERFACE
        """
        self.__write_stack.append(f"target_include_directories({for_project} {mode} {args_to_str(directories)})")
        return self

    def set(self,name:"str",value:"str")->"cmake":
        self.__write_stack.append(f"set({name} {value})")
        return self
    
    def target_link_libraries(self,lib_name:"str",name:"str"=var(project_name),mode:"str"=public)->"cmake":
        self.__write_stack.append(f"target_link_libraries({name} {mode} {lib_name})")
        return self
    
    def target_link_directories(self,name:"str"=var(project_name),mode:"str"=public,*directories:"str")->"cmake":
        self.__write_stack.append(f"target_link_directories({name} {mode} {args_to_str(directories)})")
        return self
    
    def just_add(self,sentence:"str")->"cmake":
        self.__write_stack.append(sentence)
        return self

    def file(self,new_var_name:"str",mode:"str"=glob_recurse,*search_str:"str")->"cmake":
        self.__write_stack.append(f"file({mode} {new_var_name} {args_to_str(search_str)})")
        return self