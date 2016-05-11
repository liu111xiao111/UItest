# -*- coding: utf-8 -*-

import sys,time

import logging


class Logger:

    def __init__(self,logger_name="qa.auto"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        console_handler.setFormatter(fmt)
        logger.addHandler(console_handler)
        self.logger = logger

    def d(self,msg="msg",*args):
        self.logger.debug(msg,*args)

    def i(self,msg="msg"):
        self.logger.info(msg)

    def w(self,msg="msg"):
        self.logger.warning(msg)

    def e(self,msg="msg"):
        self.logger.error(msg)


if __name__ == "__main__":
    logger = Logger();
    logger.d("hello");