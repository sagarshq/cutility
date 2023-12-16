import re


class PiiTextCleaner:
    """
    Handle Personal Identifiable Information (PII) removal/replacement tasks.

    This class provides methods to replace or remove specific types of PII from text data.
    PII includes names, emails, and contact information (phone numbers).

    Methods:
    - replace_names(text, names_list=None, repl="{{PERSON_NAME}}"):
        Replace names in the text with a specified replacement string.

    - replace_emails(text, repl="{{EMAIL}}"):
        Replace email addresses in the text with a specified replacement string.

    - replace_contacts(text, repl="{{PHONE}}"):
        Replace phone numbers in the text with a specified replacement string.

    Attributes:
    - No public attributes are required for the class.

    Example Usage:
    ```python
    pii_handler = PiiTextCleaner()
    text_with_pii = "John Doe's email is john.doe@example.com, and his phone number is +1 555-1234."

    # Replace names with a generic string
    text_without_names = pii_handler.replace_names(text_with_pii, names_list=["John Doe", "Jane Smith"])

    # Replace emails with a generic string
    text_without_emails = pii_handler.replace_emails(text_without_names)

    # Replace phone numbers with a generic string
    text_without_contacts = pii_handler.replace_contacts(text_without_emails)

    print(text_with_pii)
    print(text_without_contacts)
    ```

    Note: Ensure that the `re` module is imported before using this class.
    """

    def __init__(self):
        pass

    @staticmethod
    def replace_names(text, names_list=None, repl="{{PERSON_NAME}}"):
        """
        Replace names in the text with a specified replacement string.

        Args:
        - text (str): The input text containing names.
        - names_list (list): A list of names to be replaced.
        - repl (str): The replacement string for names.

        Returns:
        - str: The text with names replaced.

        Example:
        ```python
        pii_handler = PiiTextCleaner()
        text = "John Doe and Jane Smith are examples of names."
        text_without_names = pii_handler.replace_names(text, names_list=["John Doe", "Jane Smith"])
        print(text_without_names)
        ```
        """
        name_pattern = r"\b(?:" + "|".join(map(re.escape, names_list)) + r")\b"

        # Use re.sub() to replace the names with the replacement string
        text_with_replacements = re.sub(
            name_pattern,
            repl,
            text,
            # flags=re.IGNORECASE
        )
        return text_with_replacements

    @staticmethod
    def replace_emails(text, repl="{{EMAIL}}"):
        """
        Replace email addresses in the text with a specified replacement string.

        Args:
        - text (str): The input text containing email addresses.
        - repl (str): The replacement string for emails.

        Returns:
        - str: The text with emails replaced.

        Example:
        ```python
        pii_handler = PiiTextCleaner()
        text = "Contact us at support@example.com for assistance."
        text_without_emails = pii_handler.replace_emails(text)
        print(text_without_emails)
        ```
        """
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        text_without_emails = re.sub(email_pattern, repl, text)
        return text_without_emails

    @staticmethod
    def replace_contacts(text, repl="{{PHONE}}"):
        """
        Replace phone numbers in the text with a specified replacement string.

        Args:
        - text (str): The input text containing phone numbers.
        - repl (str): The replacement string for phone numbers.

        Returns:
        - str: The text with phone numbers replaced.

        Example:
        ```python
        pii_handler = PiiTextCleaner()
        text = "Contact us at +1 555-123-4567 or 9876543210 for assistance."
        text_without_contacts = pii_handler.replace_contacts(text)
        print(text_without_contacts)
        ```
        """
        pattern1 = r"\+[-()\s\d]+?(?=\s*[+<])"
        pattern2 = r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]"

        # Combine both patterns into a single pattern
        combined_pattern = re.compile(f"{pattern1}|{pattern2}")

        # Replace phone numbers with an empty string
        cleaned_text = combined_pattern.sub(repl, text)

        return cleaned_text
