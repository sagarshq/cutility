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

    Example Usage:
    ```python
    pii_handler = PiiTextCleaner()
    text_with_pii = "John Doe's email is john.doe@example.com, and his phone number is +1 555-1234."
    text_without_names = pii_handler.replace_names(text_with_pii, names_list=["John Doe"])
    text_without_emails = pii_handler.replace_emails(text_without_names)
    text_without_contacts = pii_handler.replace_contacts(text_without_emails)
    print(text_without_contacts)
    ```
    """

    def __init__(self):
        pass

    @staticmethod
    def replace_names(text, names_list=None, repl="{{PERSON_NAME}}"):
        """
        Replace names in the text with a specified replacement string.

        Args:
            text (str): The input text containing names.
            names_list (list): A list of names to be replaced.
            repl (str): The replacement string for names.

        Returns:
            str: The text with names replaced.

        Example Usage:
        ```python
        pii_handler = PiiTextCleaner()
        text = "John Doe and Jane Smith are examples of names."
        text_without_names = pii_handler.replace_names(text, names_list=["John Doe", "Jane Smith"])
        print(text_without_names)
        ```
        """
        name_pattern = r"\b(?:" + "|".join(map(re.escape, names_list)) + r")\b"
        text_with_replacements = re.sub(name_pattern, repl, text)
        return text_with_replacements

    @staticmethod
    def replace_emails(text, repl="{{EMAIL}}"):
        """
        Replace email addresses in the text with a specified replacement string.

        Args:
            text (str): The input text containing email addresses.
            repl (str): The replacement string for emails.

        Returns:
            str: The text with emails replaced.

        Example Usage:
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
            text (str): The input text containing phone numbers.
            repl (str): The replacement string for phone numbers.

        Returns:
            str: The text with phone numbers replaced.

        Example Usage:
        ```python
        pii_handler = PiiTextCleaner()
        text = "Contact us at +1 555-123-4567 or 9876543210 for assistance."
        text_without_contacts = pii_handler.replace_contacts(text)
        print(text_without_contacts)
        ```
        """
        pattern1 = r"\+[-()\s\d]+?(?=\s*[+<])"
        pattern2 = r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]"
        combined_pattern = re.compile(f"{pattern1}|{pattern2}")
        cleaned_text = combined_pattern.sub(repl, text)
        return cleaned_text
