__all__ = ["DirHandler"]

import os
from .dir_handler import DirHandler


def get_dir_handler(
    project_root=os.path.abspath(os.curdir),
    data_root=os.getenv("DATA_ROOT", f"{os.path.abspath(os.curdir)}/src/data"),
    config_root=os.getenv("CONFIG_ROOT", f"{os.path.abspath(os.curdir)}/src/config"),
    verbose=False,
):
    return DirHandler(project_root, data_root, config_root, verbose)
