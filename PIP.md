# pre-requisites

```bash
python -m venv pyenv
pip install twine setuptools
```

# packaging

```bash
# test locally
pip3 install .

# run setup.py
python setup.py sdist

# upload to pypi
python -m twine upload --repository pypi dist/*
```

# ref

https://www.turing.com/kb/how-to-create-pypi-packages#how-to-create-and-upload-a-package-to-pypi
