import json


def read(file_path):
    """
    Read data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data read from the JSON file.
    """
    with open(file_path, "r") as file:
        return json.load(file)
