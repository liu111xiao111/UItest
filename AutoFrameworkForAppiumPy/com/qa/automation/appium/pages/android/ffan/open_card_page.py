# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.open_card_page_configs import OpenCardPageConfigs as OCPC

class OpenCardPage(SuperPage):
    '''
    作者： 宋波
    首页=>飞凡卡=>开卡
    '''
    def __init__(self, testcase, driver, logger):
        super(OpenCardPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 检查开卡界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        OCPC.verify_view_resourceId,
                                        OCPC.verify_view_timeout)

    def validFeifanCard(self):
        '''
        usage: 验证市民公交卡
        '''
        API().assertElementByContainsText(self.testcase,
                                          self.driver,
                                          self.logger,
                                          OCPC.text_feifan_card,
                                          OCPC.verify_view_timeout)

    def validJointCard(self):
        '''
        usage : 验证一卡通飞凡联名卡
        '''
        API().assertElementByContainsText(self.testcase,
                                          self.driver,
                                          self.logger,
                                          OCPC.text_joint_card,
                                          OCPC.verify_view_timeout)

if __name__ == '__main__':
    pass;