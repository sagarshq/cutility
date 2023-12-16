from cutility.cutils import Cutils


dirh = Cutils(project_root="./", data_root="./data", verbose=True)
print(dirh.get_data_root())
print(dirh.get_project_root())
