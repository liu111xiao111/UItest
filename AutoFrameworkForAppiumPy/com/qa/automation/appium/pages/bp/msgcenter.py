#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os,sys
# reload(sys)
# sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))



from time import sleep
import unittest
from configs.driver_configs import *
from pages.bp.msgcenter_configs import *
from api.api import *
from pages.common.super_page import *

from appium import webdriver

'''
    MessageCenter 消息中心页面
'''
class MessageCenter(SuperPage):

    def __init__(self,driver,logger):
        # SuperPage.__init__(self,driver)
        super(MessageCenter, self).__init__(driver,logger)

    """
        验证消息中心textview resource id是否存在
    """
    def validSelf(self,testcase):
        API().assertViewByResourceIDUtil(test_case=testcase,driver=self.driver,
                                         resource_id=MessageCenterConfigs.resource_id_title_textview,seconds=5)

    def clickOnMsgNoticeTab(self):
        API().clickTextViewByAndroid(driver=self.driver,text=MessageCenterConfigs.text_msgNotice_textview)

    def validMsgNoticeTabSelected(self):
        #msgNotice = API().getTextViewByAndroid(driver=self.driver,text=MessageCenterConfigs.text_msgNotice_textview)
        msgNotice = API().getBrotherNodeByAndroid(driver=self.driver,text=MessageCenterConfigs.text_msgSystem_textview)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidDriver)
    unittest.TextTestRunner(verbosity=2).run(suite)