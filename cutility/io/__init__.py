"""
Expose functions
"""

__all__ = [
    "read_json",
    "read_jsonl",
    "read_text",
    "read_yaml",
    "write_json",
    "write_jsonl",
    "write_text",
    "write_yaml",
]

from .readers import _json_reader, _jsonl_reader, _text_reader, _yaml_reader
from .writers import _json_writer, _jsonl_writer, _text_writer, _yaml_writer


def read_text(file_path):
    return _text_reader.read(file_path)


def read_json(file_path):
    return _json_reader.read(file_path)


def read_jsonl(file_path):
    return _jsonl_reader.read(file_path)


def read_yaml(file_path):
    return _yaml_reader.read(file_path)


def write_text(data, file_path):
    _text_writer.write(data, file_path)


def write_json(data, file_path):
    _json_writer.write(data, file_path)


def write_jsonl(data, file_path):
    _jsonl_writer.write(data, file_path)


def write_yaml(data, file_path):
    _yaml_writer.write(data, file_path)
