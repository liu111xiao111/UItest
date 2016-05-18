# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.common.super_page import *
from com.qa.automation.appium.pages.ffan.login_page_configs import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#
#   设置页面
class SettingsPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SettingsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);


    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=LoginPageConfigs.resource_id_login_button,
                                                      seconds=10);

    def switchToNormalLogin(self):
        API().click_view_by_text_android(driver=self.driver, logger=self.logger,
                                         text=LoginPageConfigs.text_normal_login);

    def inputUserName(self):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=LoginPageConfigs.resource_id_user_name, string=LoginPageConfigs.account_name
                                               );

    def inputPassWord(self):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=LoginPageConfigs.resource_id_pass_word, string=LoginPageConfigs.account_passwd
                                               );

    def clickOnLoginBtn(self):
        API().click_view_by_resourceID_android(driver=self.driver,logger=self.logger,resource_id=LoginPageConfigs.resource_id_login_button)


if __name__ == '__main__':
    pass;
