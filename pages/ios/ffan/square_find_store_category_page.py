# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.square_find_store_category_page_configs import SquareFindStoreConfigs
from pages.logger import logger

SFSC = SquareFindStoreConfigs()

class SquareFindStorePage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>找店
    '''

    def __init__(self, testcase, driver, logger):
        super(SquareFindStorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        logger.info("Check " + SFSC.name_tv_category_tv + " begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFSC.name_tv_category_tv,
                                  SFSC.verify_view_timeout)
        logger.info("Check " + SFSC.name_tv_category_tv + " end")
        API().screenShot(self.driver, "zhaoDian")

    def validStorePage(self):
        '''
        验证找店详情页
        '''
        logger.info("Check " + SFSC.name_store_page + " begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFSC.name_store_page,
                                  SFSC.verify_view_timeout)
        logger.info("Check " + SFSC.name_store_page + " end")
        API().screenShot(self.driver, "menDianXiangQing")


    '''
        usage : 点击search
    '''
    def clickOnSearch(self):
        logger.info("Click 搜索 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SFSC.xpath_iv_search_iv)
        logger.info("Click 搜索 end")

    '''
        usage :点击第一个门店
    '''   
    def clickFirstItem(self):
        logger.info("Click 第一个门店 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SFSC.xpath_store_first_item)
        logger.info("Click 第一个门店 end")

if __name__ == '__main__':
    pass;