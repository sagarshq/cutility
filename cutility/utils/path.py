"""
Path check
"""

import os


def check_path_exist(path):
    """
    Check if a path exists.

    Args:
        path (str): The path to check.

    Returns:
        bool: True if the path exists, False otherwise.
    """
    return os.path.exists(path)
