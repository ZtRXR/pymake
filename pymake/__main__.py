from . import *

(
    cmake("3.5")
    .project("test")
    .file("SRC",glob_recurse,"*.cxx")
    .add_executable(var(project_name),var("SRC"))
    .write()
)