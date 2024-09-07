"""
Utilities for managing project paths, configurations, and directory structures.
"""

import os
import yaml
from pathlib import Path
from typing import List, Dict, Optional


class PathManager:
    """
    A utility class for managing project paths, configurations, and directory structures.
    """

    def __init__(
        self,
        project_root: str = os.getcwd(),
        data_root: str = os.getenv("DATA_ROOT", ""),
        config_root: str = os.getenv("CONFIG_ROOT", ""),
        verbose: bool = False,
    ):
        """
        Initialize the PathManager instance.

        Args:
            project_root (str): The root path of the project. Defaults to the current directory.
            data_root (str): The root path for data. Defaults to DATA_ROOT env var or project_root/src/data.
            config_root (str): The root path for configuration files. Defaults to CONFIG_ROOT env var or project_root/src/config.
            verbose (bool): If True, print information about the paths being set.
        """
        self.project_root = Path(project_root).resolve()
        self.data_root = Path(data_root or self.project_root / "src" / "data").resolve()
        self.config_root = Path(
            config_root or self.project_root / "src" / "config"
        ).resolve()
        self.config_files = list(self.config_root.glob("*.yml"))

        if verbose:
            self._print_paths()

    def _print_paths(self) -> None:
        """Print information about the paths being set."""
        print("~" * 30)
        print("Setting paths:")
        print(f"Project Root: {self.project_root}")
        print(f"Config Path: {self.config_root}")
        print(f"Config Files: {self.config_files}")
        print(f"Data Root: {self.data_root}\n")
        print("~" * 30)

    def load_yaml_config(self, config_name: str) -> Dict:
        """
        Load configuration from a YAML file.

        Args:
            config_name (str): The base name of the YAML file (without the extension).

        Returns:
            dict: A dictionary containing the configurations from the specified YAML file.

        Raises:
            FileNotFoundError: If the specified config file is not found.
            yaml.YAMLError: If there's an error parsing the YAML file.
        """
        if not self.config_files:
            raise FileNotFoundError("No config files found.")

        config_file = self.config_root / f"{config_name}.yml"
        if not config_file.exists():
            raise FileNotFoundError(f"Config file '{config_name}.yml' not found.")

        try:
            with config_file.open("r") as stream:
                return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise yaml.YAMLError(f"Error parsing YAML file: {exc}")

    def create_directory_structure(
        self, base_dir: str, subdirs: Optional[List[str]] = None
    ) -> None:
        """
        Create a directory structure in the specified base directory.

        Args:
            base_dir (str): The base directory in which to create the structure.
            subdirs (list, optional): List of subdirectories to create within the base directory.

        Raises:
            OSError: If there is an issue creating the directories.
        """
        base_path = Path(base_dir)
        if subdirs:
            for subdir in subdirs:
                (base_path / subdir).mkdir(parents=True, exist_ok=True)

    @property
    def data_root(self) -> Path:
        """Get the data root path."""
        return self._data_root

    @data_root.setter
    def data_root(self, value: Path) -> None:
        self._data_root = value

    @property
    def project_root(self) -> Path:
        """Get the project root path."""
        return self._project_root

    @project_root.setter
    def project_root(self, value: Path) -> None:
        self._project_root = value


def create_path_manager(
    project_root: str = os.getcwd(),
    data_root: str = os.getenv("DATA_ROOT", ""),
    config_root: str = os.getenv("CONFIG_ROOT", ""),
    verbose: bool = False,
) -> PathManager:
    """
    Factory function to create and return a PathManager instance.

    Args:
        project_root (str): The root path of the project. Defaults to the current directory.
        data_root (str): The root path for data. Defaults to DATA_ROOT env var or project_root/src/data.
        config_root (str): The root path for configuration files. Defaults to CONFIG_ROOT env var or project_root/src/config.
        verbose (bool): If True, print information about the paths being set.

    Returns:
        PathManager: An instance of the PathManager class.
    """
    return PathManager(project_root, data_root, config_root, verbose)


__all__ = ["PathManager", "create_path_manager"]
