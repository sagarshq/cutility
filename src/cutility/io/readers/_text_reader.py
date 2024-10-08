def read(file_path):
    """
    Read text from a plain text file.

    Args:
        file_path (str): The path to the plain text file.

    Returns:
        str: The text read from the file.

    Example Usage:
    ```python
    text = read("example.txt")
    print(text)
    ```
    """
    with open(file_path, "r") as file:
        return file.read()
