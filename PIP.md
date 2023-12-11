# pre-requisites

```bash
pip install twine setuptools
```

# packaging

```bash
python -m venv pyenv
pip3 install .
python setup.py sdist


python -m twine upload --repository pypi dist/*
```

# ref

https://www.turing.com/kb/how-to-create-pypi-packages#how-to-create-and-upload-a-package-to-pypi
