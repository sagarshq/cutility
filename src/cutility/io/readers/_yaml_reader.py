import yaml


def read(file_path):
    """
    Read data from a YAML file.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The data read from the YAML file.
    """
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
