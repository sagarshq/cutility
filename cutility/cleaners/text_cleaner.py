"""
text cleaning basic functions using regex
"""

import re
import string


class TextCleaner:
    """
    Methods:
       clean_emojis(text): Remove emojis and skin tone modifiers from the given text.
       clean_unicode_characters(text): Remove non-ASCII characters from the given text.
       clean_web_links(text): Remove web links from the given text.
       clean_profile_handle(text): Remove '@username' mentions from profile handles in the text.
       clean_hashtags(text): Remove '#' symbols from hashtags in the text.
       clean_punctuations_except(text, exceptions): Remove punctuations except specified ones in the text.
       clean_extra_spaces(text): Replace consecutive spaces with a single space in the text.
       clean_extra_newlines(text): Replace consecutive newlines with a single newline in the text.
       clean_symbols_except_punctuation(text): Remove symbols except punctuation from the text.
    """

    def __init__(self):
        pass

    @staticmethod
    def clean_emojis(text):
        """
        Remove emojis and skin tone modifiers from the given text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with emojis removed.
        """
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F700-\U0001F77F"  # alchemical symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE,
        )

        text = emoji_pattern.sub(r" ", text)
        return text

    @staticmethod
    def clean_unicode_characters(text):
        """
        Remove non-ASCII characters from the given text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with non-ASCII characters removed.
        """
        text = "".join(char for char in text if ord(char) < 128)
        return text

    @staticmethod
    def clean_web_links(text):
        """
        Remove web links from the given text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with web links removed.
        """
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"\w+.com\b", "", text)
        return text

    @staticmethod
    def clean_profile_handle(text):
        """
        Remove '@username' mentions from profile handles in the text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with '@username' mentions removed.
        """
        text = re.sub(r"@\w+", " ", text)
        return text

    @staticmethod
    def clean_hashtags(text):
        """
        Remove '#' symbols from hashtags in the text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with '#' symbols removed from hashtags.
        """
        text = re.sub(r"#\w+", " ", text)
        return text

    @staticmethod
    def clean_punctuations_except(self, exceptions):
        """
        Remove punctuations except specified ones from the text.

        Args:
            text (str): The input text.
            exceptions (list): List of punctuations to keep.

        Returns:
            str: The text with punctuations removed except specified ones.
        """
        cleaned_text = "".join(
            char if char.isalnum() or char in exceptions else " " for char in self.text
        )
        return cleaned_text

    @staticmethod
    def clean_extra_spaces(text):
        """
        Replace consecutive spaces with a single space in the text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with consecutive spaces replaced with a single space.
        """
        text = re.sub(r"[^\S\n]+", " ", text)
        return text

    @staticmethod
    def clean_extra_newlines(text):
        """
        Replace consecutive newlines with a single newline in the text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with consecutive newlines replaced with a single newline.
        """
        text = re.sub(r"\n+", "\n", text)
        return text

    @staticmethod
    def clean_symbols_except_punctuation(text):
        """
        Remove symbols except punctuation from the given text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with symbols removed except punctuation.
        """
        translator = str.maketrans("", "", string.punctuation)
        text = text.translate(translator)
        return text
