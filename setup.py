from setuptools import setup, find_packages
from setuptools_scm.version import get_local_node_and_date

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


def local_scheme(version):
    return ""


setup(
    name="cutility",
    use_scm_version={
        "local_scheme": local_scheme,  # Avoid local versions
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
    # Optional: Add entry points if you have console scripts
    # entry_points={
    #     "console_scripts": [
    #         "your_command=your_module:main_function",
    #     ],
    # },
)
