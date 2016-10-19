# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.open_card_page_configs import OpenCardPageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

OCPC = OpenCardPageConfigs()

class OpenCardPage(SuperPage):
    '''
    作者 刘涛
    首页＝>飞凡卡=>开卡
    '''
    def __init__(self, testcase, driver, logger):
        super(OpenCardPage, self).__init__(testcase,
                                           driver,
                                           logger);

    '''
        usage : 检查是否加载出来
    '''
    def validSelf(self):
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  OCPC.verify_view_resourceId,
                                  OCPC.verify_view_timeout)

    '''
        usage: 验证一卡通是否加载
    '''
    def validJointCard(self):
        jointCard = API().getTextByXpath(self.testcase,
                                         self.driver,
                                         self.logger,
                                         OCPC.xpath_joint_card)

        API().assertGreaterEqual(self.testcase,
                                 self.logger,
                                 jointCard,
                                 OCPC.text_joint_card)

    '''
        usage : 验证市民公交卡是否加载
    '''
    def validBusCard(self):
        busCard = API().getTextByXpath(self.testcase,
                                         self.driver,
                                         self.logger,
                                         OCPC.xpath_bus_card)

        API().assertGreaterEqual(self.testcase,
                                 self.logger,
                                 busCard,
                                 OCPC.text_bus_card)

if __name__ == '__main__':
    pass;