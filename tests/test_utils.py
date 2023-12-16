import cutility as cu


@cu.get_exec_time
def foo():
    import time

    time.sleep(1)


foo()

b = cu.check_path_exist("./data/temp.txt")
print(b)
