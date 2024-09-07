import logging
import sys


class Logger:
    def __init__(self, loglevel="INFO"):
        self.logger = logging.getLogger("util_logger")
        self.logger.setLevel(loglevel)

        if not self.logger.handlers:
            formatter = logging.Formatter(
                "[%(asctime)s] - [%(levelname)s] : %(message)s"
            )
            handler = logging.StreamHandler(stream=sys.stderr)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def d(self, msg):
        self.logger.debug(msg)

    def i(self, msg):
        self.logger.info(msg)

    def w(self, msg):
        self.logger.warning(msg)

    def e(self, msg):
        self.logger.error(msg)

    def c(self, msg):
        self.logger.critical(msg)
