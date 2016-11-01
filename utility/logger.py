# -*- coding: utf-8 -*-

import logging


class Logger:
    def __init__(self, logger_name='Api'):
        logger = logging.getLogger(logger_name)
        self.logger = logger

    def debug(self, msg="msg", *args):
        self.logger.debug(msg, *args)

    def info(self, msg="msg"):
        self.logger.info(msg)

    def worning(self, msg="msg"):
        self.logger.warning(msg)

    def error(self, msg="msg"):
        self.logger.error(msg)

if __name__ == "__main__":
    logger = Logger()
    logger.debug("hello")
