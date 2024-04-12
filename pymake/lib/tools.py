from typing import *
def var(name:str)->str:
    return f"${{{name}}}"

def args_to_str(args:list[str])->str:
    vars_str = ""
    for i in args:
         vars_str=f"{vars_str} {i}"
    return vars_str
