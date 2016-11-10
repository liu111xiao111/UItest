# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.store_info_page_configs import StoreInfoPageConfigs
from pages.logger import logger

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
        logger.info("Check 门店信息 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  StoreInfoPageConfigs.text_store_detail,
                                  StoreInfoPageConfigs.click_on_button_timeout)
        logger.info("Check 门店信息 begin")
        API().screenShot(self.driver, "menDianXiangQing")

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''
        API().screenShot(self.driver, "shangChao")
        logger.info("Check keywords begin")
        print("KEYWORDS: %s" % keywords)

        API().assertElementByName(self.testcase, self.driver, self.logger, keywords,
                                  StoreInfoPageConfigs.assert_view_timeout)
        logger.info("Check keywords end")

    def clickOnStoreImageTextDetails(self):
        '''
        usage: click on the store image-text button.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, StoreInfoPageConfigs.xpath_store_image_text_details_button, StoreInfoPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass;
