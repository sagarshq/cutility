# cutility

Common utils for development

# Variables

What is project_root?

- Directory that holds your src folder is your project_root

What is data_root?

- Directory that holds all your data folder is your data_root

# Usage

## Instantiate

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

# todo
