import os
from cutility import load_env

ENV = load_env("./data/.env")
print(ENV)
print(os.getenv("DATA_ROOT"))
print(os.getenv("PROJECT_ROOT"))
print(os.getenv("CONFIG_PATH"))
