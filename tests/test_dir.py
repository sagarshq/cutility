from cutility.dir import dir_handler

dirh = dir_handler.DirHandler(project_root="./", data_root="./data", verbose=True)
print(dirh.get_data_root())
print(dirh.get_project_root())
