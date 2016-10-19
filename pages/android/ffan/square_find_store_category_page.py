# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_find_store_category_page_configs import SquareFindStoreConfigs as SFSC


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
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFSC.resource_id_tv_category_tv,
                                        SFSC.verify_view_timeout)

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
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFSC.resource_id_iv_item_iv,
                                       SFSC.verify_view_timeout)
