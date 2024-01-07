from dotenv import load_dotenv


def load_env(env_path):
    """
    Load environment variables from a specified .env file.

    Args:
        env_path (str): The path to the .env file containing environment variables.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified .env file is not found.
        Exception: If there are issues loading the environment variables.
    """

    return load_dotenv(env_path)
