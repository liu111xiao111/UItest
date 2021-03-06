# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_find_store_category_page_configs import SquareFindStoreConfigs as SFSC
from api.logger import logger


class SquareFindStorePage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>找店
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareFindStorePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证找店页面
        '''
        logger.info("Check 找店页面 begin")
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFSC.text_find_store,
                                        SFSC.verify_view_timeout)
        logger.info("Check 找店页面 end")

    def clickOnSearch(self):
        '''
        usage : 点击搜索
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFSC.resource_id_iv_search_iv,
                                       SFSC.verify_view_timeout)

    def clickOnFirstItem(self):
        '''
        usage : 点击第一项商家
        '''
        logger.info("Click 第一项商家 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFSC.resource_id_iv_item_iv,
                                       SFSC.verify_view_timeout)
        logger.info("Click 第一项商家 end")
