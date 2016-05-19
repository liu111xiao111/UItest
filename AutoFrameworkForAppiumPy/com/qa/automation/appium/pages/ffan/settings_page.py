# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.common.super_page import *
from com.qa.automation.appium.pages.ffan.settings_page_configs import *

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
                                                      resource_id=SettingsPageConfigs.resource_id_setting_account_management_rl,
                                                      seconds=10);

    #点击退出当前账号button
    def clickOnQuitAccountBtn(self,confirmQuit=True):
        API().click_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SettingsPageConfigs.resource_id_setting_btn_logout_rl);
        if confirmQuit:
            API().click_view_by_text_android(driver=self.driver,logger=self.logger,text=SettingsPageConfigs.text_confirm_btn)
        else:
            API().click_view_by_text_android(driver=self.driver, logger=self.logger,
                                             text=SettingsPageConfigs.text_cancel_btn)




if __name__ == '__main__':
    pass;
