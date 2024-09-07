import json


def read(file_path):
    """
    Read data from a JSONL file.

    Args:
        file_path (str): The path to the JSONL file.

    Returns:
        list: A list of JSON objects read from the JSONL file.
    """
    with open(file_path, "r") as file:
        return [json.loads(line) for line in file]
