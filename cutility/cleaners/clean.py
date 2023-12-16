"""
Class to call all cleaners
"""

from .pii_cleaner import PiiCleaner
from .text_cleaner import TextCleaner


class GenericTextCleaner(TextCleaner, PiiCleaner):
    """
    A utility class for generic text cleaning operations, combining functionality from TextCleaner and PiiCleaner.

    Example:
    ```python
    # Create an instance of GenericTextCleaner
    generic_cleaner = GenericTextCleaner()

    # Define cleaning steps
    cleaning_steps = [
        (generic_cleaner.clean_emojis, {}),
        (generic_cleaner.clean_unicode_characters, {}),
        (generic_cleaner.clean_web_links, {}),
    ]

    # Original text
    input_text = "Check out this link: https://example.com. 😎"

    # Apply cleaning functions
    cleaned_text = generic_cleaner.apply_text_cleaning_functions(input_text, cleaning_steps)

    print("Original Text:")
    print(input_text)
    print("\nCleaned Text:")
    print(cleaned_text)
    ```

    Attributes:
    - Inherits functionality from TextCleaner and PiiCleaner.

    Methods:
    - `apply_text_cleaning_functions(input_text, cleaning_steps)`: Apply a sequence of cleaning functions to the input text.

        Args:
        - input_text (str): The original text to be cleaned.
        - cleaning_steps (list): A list of tuples, each containing a cleaning function and its arguments.

        Returns:
        - str: The text after applying all specified cleaning functions sequentially.
    """

    def __init__(self):
        """
        Initializes the GenericTextCleaner instance by calling the __init__ methods of TextCleaner and PiiCleaner.
        """
        TextCleaner.__init__(self)
        PiiCleaner.__init__(self)

    def apply_text_cleaning_functions(self, input_text, cleaning_steps):
        """
        Apply a sequence of cleaning functions to the input text.

        Args:
        - input_text (str): The original text to be cleaned.
        - cleaning_steps (list): A list of tuples, each containing a cleaning function and its arguments.

        Returns:
        - str: The text after applying all specified cleaning functions sequentially.
        """
        cleaned_text = input_text

        # Iterate through each cleaning step and apply the corresponding function
        for cleaning_func, cleaning_args in cleaning_steps:
            cleaned_text = cleaning_func(cleaned_text, **cleaning_args)

        return cleaned_text
