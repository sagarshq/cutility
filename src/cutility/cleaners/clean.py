"""
Class to call all cleaners
"""

from .pii_cleaner import PiiTextCleaner
from .text_cleaner import SimpleTextCleaner


class GenericSimpleTextCleaner(SimpleTextCleaner, PiiTextCleaner):
    """
    A utility class for generic text cleaning operations, combining functionality from SimpleTextCleaner and PiiTextCleaner.

    Example Usage:
    ```python
    generic_cleaner = GenericSimpleTextCleaner()
    cleaning_steps = [
        (generic_cleaner.clean_emojis, {}),
        (generic_cleaner.clean_unicode_characters, {}),
        (generic_cleaner.clean_web_links, {}),
    ]
    input_text = "Check out this link: https://example.com. 😎"
    cleaned_text = generic_cleaner.apply_text_cleaning_functions(input_text, cleaning_steps)
    print(cleaned_text)
    ```
    """

    def __init__(self):
        """
        Initializes the GenericSimpleTextCleaner instance by calling the __init__ methods of SimpleTextCleaner and PiiTextCleaner.
        """
        SimpleTextCleaner.__init__(self)
        PiiTextCleaner.__init__(self)

    def apply_text_cleaning_functions(self, input_text, cleaning_steps):
        """
        Apply a sequence of cleaning functions to the input text.

        Args:
            input_text (str): The original text to be cleaned.
            cleaning_steps (list): A list of tuples, each containing a cleaning function and its arguments.

        Returns:
            str: The text after applying all specified cleaning functions sequentially.
        """
        cleaned_text = input_text
        print(f"Original text: {cleaned_text}")

        for cleaning_func, cleaning_args in cleaning_steps:
            func_name = cleaning_func.__name__
            if func_name in ["replace_emails", "replace_contacts", "replace_names"]:
                cleaned_text = getattr(PiiTextCleaner, func_name)(
                    cleaned_text, **cleaning_args
                )
            else:
                cleaned_text = getattr(SimpleTextCleaner, func_name)(
                    cleaned_text, **cleaning_args
                )

        return cleaned_text
