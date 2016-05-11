# -*- coding: utf-8 -*-

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from configs.driver_configs import *
from pages.ffan.myffan_page_configs import *
from api.api import *
from common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#
#   进入应用的首页,是进入其他页面的入口
class LoginPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LoginPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入到登录页,检查登录按钮
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=login_page_configs.resource_id_login_button,
                                                      seconds=10);

    def switchToNormalLogin(self):
        API().click_view_by_text_android(driver=self.driver, logger=self.logger,
                                         text=login_page_configs.text_normal_login);

    def inputUserName(self):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               text=login_page_configs.resource_id_user_name, username
                                               );

    def inputPassWord(self):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               text=login_page_configs.resource_id_pass_word, password
                                               );


if __name__ == '__main__':
    pass;
