import os
import pytest
from pathlib import Path
from cutility.path_manager import PathManager, create_path_manager


@pytest.fixture
def temp_directory(tmp_path):
    return tmp_path


def test_path_manager_initialization(temp_directory):
    pm = PathManager(project_root=str(temp_directory))
    assert pm.project_root == temp_directory
    assert pm.data_root == temp_directory / "src" / "data"
    assert pm.config_root == temp_directory / "src" / "config"


def test_path_manager_custom_roots(temp_directory):
    data_root = temp_directory / "custom_data"
    config_root = temp_directory / "custom_config"
    pm = PathManager(
        project_root=str(temp_directory),
        data_root=str(data_root),
        config_root=str(config_root),
    )
    assert pm.project_root == temp_directory
    assert pm.data_root == data_root
    assert pm.config_root == config_root


def test_load_yaml_config(temp_directory):
    config_root = temp_directory / "config"
    config_root.mkdir()
    config_file = config_root / "test_config.yml"
    config_file.write_text("key: value")

    pm = PathManager(project_root=str(temp_directory), config_root=str(config_root))
    config = pm.load_yaml_config("test_config")
    assert config == {"key": "value"}


def test_load_yaml_config_file_not_found(temp_directory):
    pm = PathManager(project_root=str(temp_directory))
    with pytest.raises(FileNotFoundError):
        pm.load_yaml_config("non_existent_config")


def test_create_directory_structure(temp_directory):
    pm = PathManager(project_root=str(temp_directory))
    base_dir = temp_directory / "test_structure"
    subdirs = ["subdir1", "subdir2", "subdir3"]
    pm.create_directory_structure(str(base_dir), subdirs)

    for subdir in subdirs:
        assert (base_dir / subdir).is_dir()


def test_create_path_manager():
    pm = create_path_manager()
    assert isinstance(pm, PathManager)
    assert pm.project_root == Path.cwd()


def test_create_path_manager_custom_roots(temp_directory):
    data_root = temp_directory / "custom_data"
    config_root = temp_directory / "custom_config"
    pm = create_path_manager(
        project_root=str(temp_directory),
        data_root=str(data_root),
        config_root=str(config_root),
        verbose=True,
    )
    assert pm.project_root == temp_directory
    assert pm.data_root == data_root
    assert pm.config_root == config_root


def test_path_manager_properties(temp_directory):
    pm = PathManager(project_root=str(temp_directory))

    # Test getter
    assert pm.data_root == temp_directory / "src" / "data"
    assert pm.project_root == temp_directory

    # Test setter
    new_data_root = temp_directory / "new_data"
    new_project_root = temp_directory / "new_project"
    pm.data_root = new_data_root
    pm.project_root = new_project_root

    assert pm.data_root == new_data_root
    assert pm.project_root == new_project_root
