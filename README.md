# cutility

Common utilities for faster development

## Table of Contents

- [cutility](#cutility)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Utils](#utils)
      - [Measure Execution Time](#measure-execution-time)
      - [Check Path Existence](#check-path-existence)
      - [Load Environment Variables](#load-environment-variables)
    - [Loggers](#loggers)
      - [Simple Logger](#simple-logger)
    - [IO](#io)
      - [Read and Write Files](#read-and-write-files)
    - [Dir Handler](#dir-handler)
    - [Cleaners](#cleaners)
      - [Generic Cleaner](#generic-cleaner)
      - [Simple Text Cleaner](#simple-text-cleaner)
      - [PII Text Cleaner](#pii-text-cleaner)
    - [Path Manager](#path-manager)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

You can install `cutility` using pip:

```bash
pip install --upgrade cutility
```

## Usage

### Utils

#### Measure Execution Time

```python
from cutility.utils import get_exec_time

@get_exec_time
def foo():
    import time
    time.sleep(1)

foo()
# Output: Time taken to execute 'foo': 0:00:01.005044
```

#### Check Path Existence

```python
from cutility.utils import check_path_exist

exists = check_path_exist("./data/temp.txt")
print(exists)  # Output: False
```

#### Load Environment Variables

```python
from cutility.utils import load_env

ENV = load_env("./.env")
print(ENV)
print(os.getenv("DATA_ROOT"))
print(os.getenv("PROJECT_ROOT"))
print(os.getenv("CONFIG_PATH"))
```

### Loggers

#### Simple Logger

```python
from cutility.loggers import get_simple_logger

log = get_simple_logger()
log.i("Hello world of loggers")
# Output: [2023-12-17 02:21:03,847] - [INFO] : Hello world of loggers
```

### IO

#### Read and Write Files

```python
from cutility.io import readers, writers

# Read and write text files
text_content = readers.read_text("./data/example_r.txt")
writers.write_text(text_content, "./data/example_w.txt")

# Read and write JSON files
json_data = readers.read_json("./data/example_r.json")
writers.write_json(json_data, "./data/example_w.json")

# Read and write YAML files
yaml_data = readers.read_yaml("./data/example_r.yaml")
writers.write_yaml(yaml_data, "./data/example_w.yaml")
```

### Dir Handler

```python
from cutility import get_dir_handler

dirh = get_dir_handler(project_root="./", data_root="./data", verbose=True)
print(dirh.get_data_root())
print(dirh.get_project_root())
```

### Cleaners

#### Generic Cleaner

```python
from cutility.cleaners import GenericSimpleTextCleaner

gtc = GenericSimpleTextCleaner()
sample_text = """Check out this link: https://example.com. 😎 #Python @user1, sample@gmail.com 123-456-7908"""

cleaning_steps = [
    (gtc.replace_contacts, {"repl": " {{PHONE}} "}),
    (gtc.replace_emails, {"repl": " {{EMAIL}} "}),
    (gtc.clean_emojis, {}),
    (gtc.clean_hashtags, {}),
    (gtc.clean_web_links, {}),
]

cleaned_text = gtc.apply_text_cleaning_functions(sample_text, cleaning_steps)
print(cleaned_text)
```

#### Simple Text Cleaner

```python
from cutility.cleaners import SimpleTextCleaner

cleaned_text = SimpleTextCleaner.clean_emojis("🌟 Sed euismod justo t semper justo. 😊")
print(cleaned_text)
```

#### PII Text Cleaner

```python
from cutility.cleaners import PiiTextCleaner

text = "My contact number is +1(123) 456 7890 and my email is email@company.com"
cleaned_text = PiiTextCleaner.replace_emails(PiiTextCleaner.replace_contacts(text))
print(cleaned_text)
```

### Path Manager

```python
from cutility import PathManager, create_path_manager

pm = create_path_manager(project_root="./", data_root="./data", verbose=True)
print(pm.data_root)
print(pm.project_root)

# Load YAML configuration
config = pm.load_yaml_config("my_config")
print(config)

# Create directory structure
pm.create_directory_structure("./output", ["logs", "data", "results"])
```

## Project Structure

```
./src
└── cutility
    ├── __init__.py
    ├── _version.py
    ├── cleaners
    │   ├── __init__.py
    │   ├── clean.py
    │   ├── pii_cleaner.py
    │   └── text_cleaner.py
    ├── dir_handler.py
    ├── io
    │   ├── __init__.py
    │   ├── readers
    │   └── writers
    ├── loggers
    │   ├── __init__.py
    │   └── _simple_logger.py
    └── utils
        ├── __init__.py
        ├── env_loader.py
        ├── exec_time.py
        └── path.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [Apache 2.0 License](LICENSE).
