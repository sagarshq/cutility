def write(text, file_path):
    """
    Write text to a plain text file.

    Args:
        text (str): The text to be written.
        file_path (str): The path to the plain text file.

    Returns:
        None

    Example Usage:
    ```python
    write("Hello, world!", "output.txt")
    ```
    """
    with open(file_path, "w") as file:
        file.write(text)
