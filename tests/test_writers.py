import os
import json
import yaml
import tempfile
from cutility.io.writers import write_json, write_jsonl, write_text, write_yaml
from cutility.io.readers import read_json, read_jsonl, read_text, read_yaml


def test_write_json():
    data = {"key": "value"}
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as temp:
        write_json(data, temp.name)

    result = read_json(temp.name)
    os.unlink(temp.name)
    assert result == data


def test_write_jsonl():
    data = [{"key1": "value1"}, {"key2": "value2"}]
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".jsonl") as temp:
        write_jsonl(data, temp.name)

    result = read_jsonl(temp.name)
    os.unlink(temp.name)
    assert result == data


def test_write_text():
    data = "Hello, world!"
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as temp:
        write_text(data, temp.name)

    result = read_text(temp.name)
    os.unlink(temp.name)
    assert result == data


def test_write_yaml():
    data = {"key": "value", "list": [1, 2, 3]}
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml") as temp:
        write_yaml(data, temp.name)

    result = read_yaml(temp.name)
    os.unlink(temp.name)
    assert result == data
