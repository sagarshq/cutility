# pre-requisites

```bash
python -m venv pyenv
pip install twine setuptools
```

# packaging

```bash
# test locally
pip install . --no-cache-dir

# run setup.py
python setup.py sdist

# upload to pypi
python -m twine upload --repository pypi dist/*
```

# cleanup

```bash

# rm __pycache__
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```

# ref

https://www.turing.com/kb/how-to-create-pypi-packages#how-to-create-and-upload-a-package-to-pypi
