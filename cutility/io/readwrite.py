"""
Read Write utility functions
"""

import json
import yaml


class ReadWrite:
    """
    ReadWrite is a utility class providing methods for reading from and writing to different file formats.

    Attributes:
        None

    Methods:
        read_json(file_path): Read data from a JSON file.
        read_yaml(file_path): Read data from a YAML file.
        read_txt(file_path): Read text from a plain text file.
        write_json(data, file_path, indent=2): Write data to a JSON file with optional indentation.
        write_yaml(data, file_path): Write data to a YAML file.
        write_txt(text, file_path): Write text to a plain text file.
    """

    def read_json(file_path):
        """
        Read data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The data read from the JSON file.
        """
        with open(file_path, "r") as file:
            return json.load(file)

    def read_yaml(file_path):
        """
        Read data from a YAML file.

        Args:
            file_path (str): The path to the YAML file.

        Returns:
            dict: The data read from the YAML file.
        """
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def read_txt(file_path):
        """
        Read text from a plain text file.

        Args:
            file_path (str): The path to the plain text file.

        Returns:
            str: The text read from the file.
        """
        with open(file_path, "r") as file:
            return file.read()

    def write_json(data, file_path, indent=2):
        """
        Write data to a JSON file with optional indentation.

        Args:
            data (dict): The data to be written.
            file_path (str): The path to the JSON file.
            indent (int): The number of spaces for indentation (default is 2).

        Returns:
            None
        """
        with open(file_path, "w") as file:
            json.dump(data, file, indent=indent)

    def write_yaml(data, file_path):
        """
        Write data to a YAML file.

        Args:
            data (dict): The data to be written.
            file_path (str): The path to the YAML file.

        Returns:
            None
        """
        with open(file_path, "w") as file:
            yaml.dump(data, file, default_flow_style=False)

    def write_txt(text, file_path):
        """
        Write text to a plain text file.

        Args:
            text (str): The text to be written.
            file_path (str): The path to the plain text file.

        Returns:
            None
        """
        with open(file_path, "w") as file:
            file.write(text)
