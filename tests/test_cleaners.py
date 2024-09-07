from cutility.cleaners import (
    SimpleTextCleaner,
    PiiTextCleaner,
    GenericSimpleTextCleaner,
)


def test_simple_text_cleaner():
    text = "Hello 😊 world! #hashtag @username"
    cleaned = SimpleTextCleaner.clean_emojis(text)
    assert "😊" not in cleaned

    cleaned = SimpleTextCleaner.clean_hashtags(text)
    assert "#hashtag" not in cleaned

    cleaned = SimpleTextCleaner.clean_profile_handle(text)
    assert "@username" not in cleaned


def test_pii_text_cleaner():
    text = "Contact John Doe at john.doe@example.com or 123-456-7890"
    cleaned = PiiTextCleaner.replace_emails(text)
    assert "john.doe@example.com" not in cleaned

    cleaned = PiiTextCleaner.replace_contacts(text)
    assert "123-456-7890" not in cleaned


def test_generic_simple_text_cleaner():
    cleaner = GenericSimpleTextCleaner()
    text = "Hello 😊 world! #hashtag @username john.doe@example.com 123-456-7890"

    cleaning_steps = [
        (cleaner.replace_emails, {"repl": "{{EMAIL}}"}),
        (cleaner.replace_contacts, {"repl": "{{PHONE}}"}),
        (cleaner.clean_emojis, {}),
        (cleaner.clean_hashtags, {}),
        (cleaner.clean_profile_handle, {}),
    ]

    cleaned = cleaner.apply_text_cleaning_functions(text, cleaning_steps)
    assert "😊" not in cleaned
    assert "#hashtag" not in cleaned
    assert "@username" not in cleaned
    assert "john.doe@example.com" not in cleaned
    assert "123-456-7890" not in cleaned
    assert "{{EMAIL}}" in cleaned
    assert "{{PHONE}}" in cleaned

    print(f"Final cleaned text: {cleaned}")
