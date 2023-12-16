"""
Measure exectution time of a function
"""

from datetime import datetime


def get_exec_time(func):
    """
    Decorator function to measure the execution time of another function.

    Args:
        func (callable): The function to be measured.

    Returns:
        callable: The wrapper function that measures and prints the execution time.
    """

    def wrapper(*args, **kwargs):
        t0 = datetime.now()
        result = func(*args, **kwargs)
        t1 = datetime.now()
        execution_time = t1 - t0
        print(f"Time taken to execute '{func.__name__}': {execution_time}")
        return result

    return wrapper
