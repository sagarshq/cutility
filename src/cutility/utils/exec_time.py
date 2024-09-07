"""
Measure exectution time of a function
"""

import time
from functools import wraps


def get_exec_time(func):
    """
    Decorator function to measure the execution time of another function.

    Args:
        func (callable): The function to be measured.

    Returns:
        callable: The wrapper function that measures and prints the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Time taken to execute '{func.__name__}': {end_time - start_time:.6f} seconds"
        )
        return result

    return wrapper
