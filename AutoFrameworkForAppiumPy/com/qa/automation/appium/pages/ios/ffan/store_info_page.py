# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.store_info_page_configs import StoreInfoPageConfigs


class StoreInfoPage(SuperPage):
    '''
    作者 宋波
    首页=>搜索页=>门店信息
    '''

    def __init__(self, testcase, driver, logger):
        super(StoreInfoPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查是否加载出来
    '''

    def validSelf(self):
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  StoreInfoPageConfigs.text_store_detail,
                                  StoreInfoPageConfigs.click_on_button_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assertElementByName(self.testcase, self.driver, self.logger, keywords,
                                  StoreInfoPageConfigs.assert_view_timeout)

    def clickOnStoreImageTextDetails(self):
        '''
        usage: click on the store image-text button.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, StoreInfoPageConfigs.xpath_store_image_text_details_button, StoreInfoPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass;
