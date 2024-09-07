from setuptools import setup, find_packages

# Dynamically install setuptools_scm if not available
try:
    from setuptools_scm import get_version
except ImportError:
    import subprocess

    subprocess.check_call(["pip", "install", "setuptools_scm"])
    from setuptools_scm import get_version

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


def local_scheme(version):
    return ""


setup(
    name="cutility",
    use_scm_version={
        "local_scheme": local_scheme,
        "write_to": "src/cutility/_version.py",
    },
    setup_requires=["setuptools>=42", "setuptools_scm"],
    author="Sagar Sarkale",
    author_email="sagarsarkale.work@gmail.com",
    description="Common Utility functions for development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sagarshq/cutility",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=["simplejson", "pyyaml", "python-dotenv"],
)
