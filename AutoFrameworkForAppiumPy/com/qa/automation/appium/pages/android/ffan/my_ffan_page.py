# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.ffan.my_ffan_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   进入应用的首页,是进入其他页面的入口
class MyFfanPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(MyFfanPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    '''
        usage : 进入到应用首页,检查ffan logo
    '''
    def validSelf(self):
        API().assert_view_by_text_android(testcase = self.testcase , driver = self.driver,
                                          logger = self.logger ,
                                          text=MyFfanPageConfigs.text_my_ffan);


    def clickOnLogin(self):
        API().click_view_by_resourceID_android(driver = self.driver,logger=self.logger,resource_id=MyFfanPageConfigs.resource_id_tv_login_tv);


    def validLoginStatus(self):
        API().assert_view_by_resourceID_Until_android(testcase=self.testcase,logger=self.logger,driver=self.driver,resource_id=MyFfanPageConfigs.resource_id_txt_user_nick_name_tv,seconds=90)

    def clickOnSettings(self):
        API().scroll_to_text(driver=self.driver,logger=self.logger,text=MyFfanPageConfigs.text_settins)
        API().click_view_by_text_android(driver=self.driver,logger=self.logger,text=MyFfanPageConfigs.text_settins)


if __name__ == '__main__':
    pass;