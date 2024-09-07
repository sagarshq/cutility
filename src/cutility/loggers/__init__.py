"""
Expose functions
"""
__all__ = [
    "get_simple_logger",
]

from ._simple_logger import Logger


def get_simple_logger(loglevel="INFO"):
    return Logger(loglevel)
