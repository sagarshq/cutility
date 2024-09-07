import json


def write(data, file_path, indent=2):
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
