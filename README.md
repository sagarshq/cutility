# cutility

Common utils for faster development

# Installation

You can install `cutility` using pip:

```bash
# to update to latest version
pip install --upgrade cutility
```

# Usage

## utils

### Measure Execution Time

```python
import cutility as cu

@cu.get_exec_time
def foo():
    import time
    time.sleep(1)

foo()
```

Output:

```markdown
Time taken to execute 'foo': 0:00:01.005044
```

### Check Path Existence

```python
import cutility as cu

b = cu.check_path_exist("./data/temp.txt")
print(b)
```

Output:

```markdown
False
```

## logger

### simple logger

```python
import cutility as cu

# Create a simple logger instance
log = cu.get_simple_logger()

# Log an information message
log.i("hello world of loggers")

# also supports warning critical debug error messages
# log.i, log.d, log.w, log.e, log.c
```

```log
# output
[2023-12-17 02:21:03,847] - [INFO] : hello world of loggers
```

## io

### read write files

Read write files. Currently supports only 3 formats:

- text
- json
- yaml

```python

import cutility as cu

# Example 1: Reading and Writing a text file
file_content = cu.read_text("./data/example_r.txt")
cu.write_text(file_content, "./data/example_w.txt")

# Example 2: Reading and Writing a JSON file
json_data = cu.read_json("./data/example_r.json")
cu.write_json(json_data, "./data/example_w.json")


# Example 3: Reading and Writing a YAML file
yaml_data = cu.read_yaml("./data/example_r.yaml")
cu.write_yaml(yaml_data, "./data/example_w.yaml")
```

## data

### dir handler

Method to standardize access to folders and configs

What is `project_root`?

- Directory that holds your src folder is your `project_root`

What is `data_root`?

- Directory that holds all your data folder is your `data_root`

```python
from cutility.cutils import Cutils

# Create an instance of Cutils
dirh = Cutils(project_root="./", data_root="./data", verbose=True)

# Print project and data root paths
DATA_ROOT = dirh.get_data_root()
PROJECT_ROOT = dirh.get_project_root()
```

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting paths:
Project Root: ./
Config Path: /path/to/config
Config Files: [list of config files]
Data Root: ./data

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

## Cleaner

### Generic cleaner

Use this snippet to collectively apply multiple cleaning functions

```python
from cutility.cleaners import GenericSimpleTextCleaner
from typing import List, Dict, Tuple, Any, Callable

# Create an instance of GenericSimpleTextCleaner
gtc = GenericSimpleTextCleaner()

# Sample text
sample_text = """Check out this link: https://example.com. 😎 #Python @user1, sample@gmail.com 123-456-7908 #testing # python"""

# List of names for name replacement
names_list = ["John", "Doe", "Jane", "Smith"]

# Define cleaning steps
all_cleaning_steps = [
    (gtc.replace_contacts, {"repl": " {{PHONE}} "}),
    (gtc.replace_emails, {"repl": " {{EMAIL}} "}),
    (gtc.replace_names, {"names_list": names_list, "repl": " {{PERSON_NAME}} "}),
    (gtc.clean_emojis, {}),
    (gtc.clean_extra_newlines, {}),
    (gtc.clean_extra_spaces, {}),
    (gtc.clean_hashtags, {}),
    (gtc.clean_profile_handle, {}),
    (gtc.clean_punctuations_except, {"exceptions": [",", ".", "\n", "?", "}", "{"]}),
    (gtc.clean_unicode_characters, {}),
    (gtc.clean_web_links, {}),
]

# Apply text cleaning functions
output = gtc.apply_text_cleaning_functions(sample_text, all_cleaning_steps)

# Print the original and cleaned text
print(sample_text)
print()
print(output)
```

### Simple Text cleaner

Use this snippet to individually apply simple cleaning functions

```python
# simpler text cleaner
from cutility.cleaners import SimpleTextCleaner as stc

t = stc.clean_emojis("🌟 Sed euismod justo t semper justo. 😊")
print(t)

```

### PII Text cleaner

Use this snippet to individually apply PII cleaning functions

```python
from cutility.cleaners import PiiTextCleaner as ptc

t = ptc.replace_emails(
    ptc.replace_contacts(
        "My contact number is +1(123) 456 7890 and my email is email@company.com"
    )
)
print(t)
```

# Appendix

## Getting names_list

I have curated list of first names and last names

- public github databases and compiled it here in a github gist.
- references mentioned in the end

Use this command to get names data.

```bash
wget https://gist.githubusercontent.com/sagarsrc/e6c7361f9ba6a64b2c9ac5bb10f0285a/raw/fbcca7c6821e7aff285271a6ce42361bbe95cc0c/pii_names.json
```

# References

[1] Datasets - [~160k first names ~100k last names](https://github.com/Debdut/names.io) - [Indian Names dataset](https://github.com/MASTREX/List-of-Indian-Names)
