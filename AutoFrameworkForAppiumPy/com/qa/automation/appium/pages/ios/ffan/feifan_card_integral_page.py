# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.feifan_card_integral_page_configs import FeiFanCardIntegralPageConfigs

class FeiFanCardIntegralPage(SuperPage):
    '''
    作者 刘涛
    首页＝>飞凡卡=>积分
    '''

    def __init__(self, testcase, driver, logger):
        super(FeiFanCardIntegralPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
            usage : 判断"我的非凡积分"页是否正确显示
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=FeiFanCardIntegralPageConfigs.name_integral)


if __name__ == '__main__':
    pass;