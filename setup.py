from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="cutility",
    version="0.1.2",
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
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "simplejson",
        # "jsonl",
        "pyyaml",
        # Add other dependencies here if needed
    ],
)
