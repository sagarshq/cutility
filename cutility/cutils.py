"""
common utils
"""

import os
import yaml
from datetime import datetime
from glob import glob


class Cutils:
    """
    A utility class providing common functionalities for working with
    configurations, paths, directories, and function execution time.
    """

    def __init__(
        self,
        project_root=os.path.abspath(os.curdir),
        data_root=os.getenv("DATA_ROOT", f"{os.path.abspath(os.curdir)}/src/data"),
        config_root=os.getenv(
            "CONFIG_ROOT", f"{os.path.abspath(os.curdir)}/src/config"
        ),
        verbose=False,
    ):
        """
        Initializes the Cutils instance.

        Args:
            project_root (str): The root path of the project. Defaults to the current directory.
            data_root (str): The root path for data.
                Defaults to the value of the "DATA_ROOT" environment variable,
                or the 'data' subdirectory of the current directory if the variable is not set.
            config_root (str): The root path for configuration files.
                Defaults to the value of the "CONFIG_ROOT"
                environment variable, or the 'config' subdirectory of the current directory
                if the variable is not set.
            verbose (bool): If True, print information about the paths being set.
        """
        self.project_root = project_root
        self.config_root = config_root
        self.data_root = data_root
        self.config_files = glob(f"{self.config_root}/*.yml")

        if verbose:
            print("~" * 30)
            print("Setting paths:")
            print(f"Project Root: {self.project_root}")
            print(f"Config Path: {self.config_root}")
            print(f"Config Files: {self.config_files}")
            print(f"Data Root: {self.data_root}\n")
            print("~" * 30)

    def get_yml_config(self, keyname: str):
        """
        Get configuration from a YAML file.

        Args:
            keyname (str): The base name of the YAML file (without the extension).

        Returns:
            dict: A dictionary containing the configurations from the specified YAML file.
        """

        if len(self.config_files) > 0:
            files_dict = {
                os.path.basename(i).replace(".yml", ""): i for i in self.config_files
            }
            fpath = files_dict.get(keyname, "__DEFAULT__")

            with open(fpath, "r") as stream:
                try:
                    config = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)

            return config
        else:
            return "No config file found"

    def get_data_root(self):
        """
        Get the data root path.

        Returns:
            str: The data root path.
        """
        return self.data_root

    def get_project_root(self):
        """
        Get the project root path.

        Returns:
            str: The project root path.
        """
        return self.project_root

    def make_directory_structure(self, prefix: str, local_paths: list = None):
        """
        Create directory structure in the specified prefix directory.

        Args:
            prefix (str): The directory in which you want to add directories.
            local_paths (list, optional): List of local paths to create within the specified prefix directory.
                Defaults to None.

        Raises:
            OSError: If there is an issue creating the directories.

        Example:
            To create a directory structure in the 'project_root' with specific paths:

            ```python
            cutils_instance = Cutils()
            cutils_instance.make_directory_structure(cutils_instance.project_root, ['dir1', 'dir2'])
            ```

            This will create the following structure:
            ```
            /path/to/project_root
                ├── dir1
                └── dir2
            ```
        """
        if local_paths is not None:
            for p in local_paths:
                os.makedirs(f"{prefix}/{p}", exist_ok=True)

    @staticmethod
    def check_path_exist(path):
        """
        Check if a path exists.

        Args:
            path (str): The path to check.

        Returns:
            bool: True if the path exists, False otherwise.
        """
        return os.path.exists(path)

    @staticmethod
    def measure_time(func):
        """
        Decorator function to measure the execution time of another function.

        Args:
            func (callable): The function to be measured.

        Returns:
            callable: The wrapper function that measures and prints the execution time.
        """

        def wrapper(*args, **kwargs):
            t0 = datetime.now()
            result = func(*args, **kwargs)
            t1 = datetime.now()
            execution_time = t1 - t0
            print(f"Time taken to execute '{func.__name__}': {execution_time}")
            return result

        return wrapper
