from cutility.cleaners import GenericTextCleaner


gtc = GenericTextCleaner()

sample_text = """Check out this link: https://example.com. 😎 #Python @user1, sample@gmail.com 123-456-7908 #testing # python"""

names_list = ["John", "Doe", "Jane", "Smith"]

all_cleaning_steps = [
    # pii cleaning
    (gtc.replace_contacts, {"repl": " {{CONTACT}} "}),
    (gtc.replace_emails, {"repl": " {{EMAIL}} "}),
    (gtc.replace_names, {"names_list": names_list, "repl": " {{PERSON_NAME}} "}),
    # text cleaning
    (gtc.clean_emojis, {}),
    (gtc.clean_extra_newlines, {}),
    (gtc.clean_extra_spaces, {}),
    (gtc.clean_hashtags, {}),
    (gtc.clean_profile_handle, {}),
    (
        gtc.clean_punctuations_except,
        {"exceptions": [",", ".", "\n", "?", "}", "{"]},
    ),
    (gtc.clean_unicode_characters, {}),
    (gtc.clean_web_links, {}),
]

output = gtc.apply_text_cleaning_functions(sample_text, all_cleaning_steps)

print(sample_text)
print()
print(output)


print("-" * 30)
# individual tests
t = gtc.clean_emojis("🌟 Sed euismod justo t semper justo. 😊")
print(t)

print("-" * 30)
# individual tests
t = gtc.replace_contacts("My contact number is +1(123) 456 7890")
print(t)
