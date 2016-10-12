# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.supermarket_page_configs import SupermarketPageConfigs as SMPC


class SupermarketPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>商超
    '''
    def __init__(self, testcase, driver, logger):
        super(SupermarketPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证商超页面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMPC.text_supermarket_title,
                                  SMPC.assert_view_timeout)

        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMPC.text_supermarket_tab_title,
                                  SMPC.assert_view_timeout)

        listNumber = len(API().getElementsByType(testCase=self.testcase,
                                                 driver=self.driver,
                                                 logger=self.driver,
                                                 elementType=SMPC.type_supermarket))

        API().assertGreaterEqual(testCase=self.testcase,
                                 logger=self.logger,
                                 listLength=listNumber,
                                 expectNum=SMPC.SUPERMARKETNUMBER)
