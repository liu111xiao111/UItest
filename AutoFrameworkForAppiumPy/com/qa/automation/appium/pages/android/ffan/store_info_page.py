# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.store_info_page_configs import StoreInfoPageConfigs as SIPC


class StoreInfoPage(SuperPage):
    '''
    作者 宋波
    首页=>搜索页=>门店信息
    '''
    def __init__(self, testcase, driver, logger):
        super(StoreInfoPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 检查是否加载出来
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SIPC.text_store_detail,
                                  SIPC.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementByContainsText(self.testcase,
                                          self.driver,
                                          self.logger,
                                          keywords,
                                          SIPC.assert_view_timeout)

    def clickOnStoreImageTextDetails(self):
        '''
        usage: 点击门店图片
        '''

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SIPC.xpath_store_image_text_details_button,
                                  SIPC.click_on_button_timeout)
