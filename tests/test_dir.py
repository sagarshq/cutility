from cutility import get_dir_handler

dirh = get_dir_handler(project_root="./", data_root="./data", verbose=True)
print(dirh.get_data_root())
print(dirh.get_project_root())
