import os
import json
import yaml
import tempfile
from cutility.io.readers import read_json, read_jsonl, read_text, read_yaml


def test_read_json():
    data = {"key": "value"}
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as temp:
        json.dump(data, temp)

    result = read_json(temp.name)
    os.unlink(temp.name)
    assert result == data


def test_read_jsonl():
    data = [{"key1": "value1"}, {"key2": "value2"}]
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".jsonl") as temp:
        for item in data:
            temp.write(json.dumps(item) + "\n")

    result = read_jsonl(temp.name)
    os.unlink(temp.name)
    assert result == data


def test_read_text():
    data = "Hello, world!"
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as temp:
        temp.write(data)

    result = read_text(temp.name)
    os.unlink(temp.name)
    assert result == data


def test_read_yaml():
    data = {"key": "value", "list": [1, 2, 3]}
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml") as temp:
        yaml.dump(data, temp)

    result = read_yaml(temp.name)
    os.unlink(temp.name)
    assert result == data
