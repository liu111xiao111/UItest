# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.open_card_page_configs import OpenCardPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

OCPC = OpenCardPageConfigs()

'''
    usage: 飞凡卡
'''
class OpenCardPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(OpenCardPage, self).__init__(testcase,
                                           driver,
                                           logger);

    '''
        usage : 检查是否加载出来
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              OCPC.verify_view_resourceId,
                                              OCPC.verify_view_timeout)

    '''
        usage: 验证飞凡标准卡是否加载
    '''
    def validFeifanCard(self):
        API().assert_view_by_text_contains_android(self.testcase,
                                                   self.driver,
                                                   self.logger,
                                                   OCPC.text_feifan_card)

    '''
        usage : 验证一卡通是否加载
    '''
    def validJointCard(self):
        API().assert_view_by_text_contains_android(self.testcase,
                                                   self.driver,
                                                   self.logger,
                                                   OCPC.text_joint_card)

if __name__ == '__main__':
    pass;