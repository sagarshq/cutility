import os
import time
from cutility import get_exec_time, check_path_exist, load_env


def test_get_exec_time(capsys):
    @get_exec_time
    def dummy_function():
        time.sleep(0.1)

    dummy_function()
    captured = capsys.readouterr()
    assert "Time taken to execute 'dummy_function'" in captured.out


def test_check_path_exist():
    assert check_path_exist(__file__) == True
    assert check_path_exist("non_existent_file.txt") == False


def test_load_env():
    with open(".env_test", "w") as f:
        f.write("TEST_VAR=test_value\n")

    load_env(".env_test")
    assert os.getenv("TEST_VAR") == "test_value"
    os.remove(".env_test")
