#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os,sys
# reload(sys)
# sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))



from time import sleep
import unittest
from configs.driver_configs import *
from pages.bp.dashboard_configs import *
from api.api import *
from pages.common.super_page import *

from appium import webdriver

'''
    Dashboard 页面是商户应用的第一个页面,相当于一个跳转页面
'''
class Dashboard(SuperPage):

    def __init__(self,driver,logger):
        # SuperPage.__init__(self,driver)
        super(Dashboard, self).__init__(driver)
        self.logger = logger

    """
        点击消息tab
    """
    def clickOnMessageTextView(self):
        API().clickTextViewByAndroid(driver=self.driver,text=DashboardConfigs.text_msg_textview)

    """
        点击设置tab
    """
    def clickOnSettingsTextView(self):
        API().clickTextViewByAndroid(driver=self.driver, text=DashboardConfigs.text_settings_textview)

    """
        点击设置首页
    """
    def clickOnSettingsTextView(self):
        API().clickTextViewByAndroid(driver=self.driver, text=DashboardConfigs.text_firstPage_textview)

    def validSelf(self,testcase):
        # API().assertViewByResourceID(test_case=testcase,driver=self.driver,resource_id=DashboardConfigs.resource_id_title_textview)
        API().assertViewByResourceIDUntil(test_case=testcase,driver=self.driver,resource_id=DashboardConfigs.resource_id_title_textview,seconds=5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidDriver)
    unittest.TextTestRunner(verbosity=2).run(suite)