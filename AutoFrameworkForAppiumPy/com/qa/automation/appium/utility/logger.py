#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import sys,time
reload(sys)
sys.setdefaultencoding('utf8')

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

    def d(self,msg="msg"):
        self.logger.debug(msg)

    def i(self,msg="msg"):
        self.logger.info(msg)

    def w(self,msg="msg"):
        self.logger.warning(msg)

    def e(self,msg="msg"):
        self.logger.error(msg)