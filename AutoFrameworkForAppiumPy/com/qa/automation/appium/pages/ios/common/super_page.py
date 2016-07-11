# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API


class SuperPage(object):
    def __init__(self, testcase, driver, logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def waitBySeconds(self, seconds=1):
        API().wait_by_seconds(seconds);

    def clickBackKey(self):
        API().click_back_key_ios(self.testcase, self.driver, self.logger,
                                 "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")

if __name__ == '__main__':
    pass
