# cutility

Common utils for development

## Installation

You can install TextCleaner using pip:

```bash
# install cutility
pip install cutility
```

```bash
# latest version
pip install --upgrade cutility
```

## Variables

What is `project_root`?

- Directory that holds your src folder is your `project_root`

What is `data_root`?

- Directory that holds all your data folder is your `data_root`

# Usage

## data folders and logger

```python
from cutility import cutils, logger

# add data folder as per your preference
# add config folder as per your preference
cu = cutils.Cutils(
                    data_root=f"path/to/data/folder",
                    config_root=f"path/to/config/folder", # currently only supports .yml files
                    verbose=True
)


log = logger.Logger()
log.i("This is info message")
# also supports warning critical debug messages
```

## Getting names_list

I have curated list of first names and last names from public github databases and compiled it here in a github gist.
Use this command to get names data.

```bash
wget https://gist.githubusercontent.com/sagarsrc/e6c7361f9ba6a64b2c9ac5bb10f0285a/raw/fbcca7c6821e7aff285271a6ce42361bbe95cc0c/pii_names.json
```

## Generic cleaner

Use this snippet to collectively apply multiple cleaning functions

```python

all_cleaning_steps = [
    # text cleaning
    (tc.clean_emojis, {}),
    (tc.clean_extra_newlines, {}),
    (tc.clean_extra_spaces, {}),
    (tc.clean_hashtags, {}),
    (tc.clean_profile_handle, {}),
    (tc.clean_symbols_except_punctuation, {}),
    (tc.clean_unicode_characters, {}),
    (tc.clean_web_links, {}),
    # pii cleaning
    (pii.replace_contacts, {"repl": " {{CONTACT}} "}),
    (pii.replace_emails, {"repl": " {{EMAIL}} "}),
    (pii.replace_names, {"names_list": names_list, "repl": " {{PERSON_NAME}} "}),
]

```

## Text cleaner

Use this snippet to individually apply simple cleaning functions

```python
# Import the TextCleaner class
from cleaners.text_cleaner import TextCleaner

# Create an instance of TextCleaner
tc = TextCleaner()

# Sample text for demonstration
sample_text = "Check out this link: https://example.com. 😎 #Python @user1"

# Step 1: Clean web links
text_without_links = tc.clean_web_links(sample_text)

# Step 2: Clean profile handles
text_without_handles = tc.clean_profile_handle(text_without_links)

# Step 3: Clean hashtags
text_without_hashtags = tc.clean_hashtags(text_without_handles)

# Step 4: Clean emojis
text_without_emojis = tc.clean_emojis(text_without_hashtags)

# Step 5: Clean extra spaces
final_cleaned_text = tc.clean_extra_spaces(text_without_emojis)
```

```python
# output
'Check out this link: '
```

## PII cleaner

Use this snippet to individually apply PII cleaning functions

```python
from cleaners.pii_cleaner import PiiCleaner
pc = PiiCleaner()
text_with_pii = "John's email is john.doe@example.com, and his phone number is +1 555-1234."

# Replace names with a generic string
text_without_names = pc.replace_names(text_with_pii, names_list=["John", "Doe", "Jane", "Smith"], repl='{{PERSON_NAME}}')

# Replace emails with a generic string
text_without_emails = pc.replace_emails(text_without_names, repl='{{EMAIL}}')

# Replace phone numbers with a generic string
text_without_contacts = pc.replace_contacts(text_without_emails, repl='{{PHONE}}')

print(text_with_pii)
print(text_without_contacts)
```

```python
# output
"{{PERSON_NAME}}'s email is {{EMAIL}}, and his phone number is {{PHONE}}."
```
