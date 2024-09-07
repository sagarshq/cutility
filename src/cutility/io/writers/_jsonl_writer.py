import json


def write(data, file_path):
    """
    Write data to a JSONL file.

    Args:
        data (list): A list of JSON-serializable objects to be written.
        file_path (str): The path to the JSONL file.

    Returns:
        None
    """
    with open(file_path, "w") as file:
        for item in data:
            json.dump(item, file)
            file.write("\n")
