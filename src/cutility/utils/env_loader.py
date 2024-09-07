from dotenv import load_dotenv


def load_env(env_path):
    """
    Load environment variables from a specified .env file.

    Args:
        env_path (str): The path to the .env file containing environment variables.

    Returns:
        None

    Example Usage:
    ```python
    load_env(".env")
    ```
    """
    return load_dotenv(env_path)
