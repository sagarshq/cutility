import os
import sys
import logging


class Logger:
    """
    A simple logger utility for setting up and using a logger with customizable log levels.

    The logger uses the environment variable `LOG_LEVEL` to set the desired logging level. If the variable is not
    set, it defaults to "INFO".

    Log Levels:
        - CRITICAL: 50
        - ERROR: 40
        - WARNING: 30
        - INFO: 20
        - DEBUG: 10
        - NOTSET: 0

    Attributes:
        logger (logging.Logger): The logger instance.

    Methods:
        __init__(loglevel='INFO'):
            Initializes the Logger instance.
            Args:
                loglevel (str): The default logging level. Defaults to 'INFO'.

        d(msg):
            Log a message at the DEBUG level.
            Args:
                msg (str): The message to be logged.

        i(msg):
            Log a message at the INFO level.
            Args:
                msg (str): The message to be logged.

        w(msg):
            Log a message at the WARNING level.
            Args:
                msg (str): The message to be logged.

        e(msg):
            Log a message at the ERROR level.
            Args:
                msg (str): The message to be logged.

        c(msg):
            Log a message at the CRITICAL level.
            Args:
                msg (str): The message to be logged.
    """

    def __init__(self, loglevel="INFO"):
        """
        Initializes the Logger instance.

        Args:
            loglevel (str): The default logging level. Defaults to 'INFO'.
        """

        # get log level
        loglevel = os.getenv("LOG_LEVEL", loglevel)

        # create logger
        self.logger = logging.getLogger("util_logger")
        self.logger.propagate = False
        self.logger.handlers = []
        self.logger.setLevel(loglevel)

        # create console handler and set level to debug
        ch = logging.StreamHandler(sys.stderr)
        ch.setLevel(loglevel)

        # create formatter
        formatter = logging.Formatter("[%(asctime)s] - [%(levelname)s] : %(message)s")

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)

    def d(self, msg):
        """
        Log a message at the DEBUG level.

        Args:
            msg (str): The message to be logged.
        """
        self.logger.debug(msg)

    def i(self, msg):
        """
        Log a message at the INFO level.

        Args:
            msg (str): The message to be logged.
        """
        self.logger.info(msg)

    def w(self, msg):
        """
        Log a message at the WARNING level.

        Args:
            msg (str): The message to be logged.
        """
        self.logger.warning(msg)

    def e(self, msg):
        """
        Log a message at the ERROR level.

        Args:
            msg (str): The message to be logged.
        """
        self.logger.error(msg)

    def c(self, msg):
        """
        Log a message at the CRITICAL level.

        Args:
            msg (str): The message to be logged.
        """
        self.logger.critical(msg)
