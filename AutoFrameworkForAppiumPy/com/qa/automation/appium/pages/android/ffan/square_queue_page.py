# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.square_queue_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SquareQueuePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareQueuePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Click "排队取号" in square page, and load "排队取号" correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SquareQueuePageConfigs.resource_id_queue, seconds=18);

    def clicOnQueueNumber(self):
        '''
        usage: Click "取号"
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareQueuePageConfigs.text_queue_number);

    def inputNumberOfMeals(self):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SquareQueuePageConfigs.resource_id_number_of_meals,
                                               string=SquareQueuePageConfigs.number_of_meals
                                               );

    def clicOnGetQueueNumber(self):
        '''
        usage: Click "一键取号"
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareQueuePageConfigs.text_get_queue_number);


if __name__ == '__main__':
    pass;
