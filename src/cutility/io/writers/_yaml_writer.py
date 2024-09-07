import yaml


def write(data, file_path):
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
