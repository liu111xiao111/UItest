#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import operator

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.stores_and_supermarkets_page_configs import StoresAndSupermarketsPageConfigs as SASPC


class StoresAndSupermarketsPage(SuperPage):
    '''
    作者 刘涛
    首页=>商超
    '''

    def __init__(self, testcase, driver, logger):
        '''
        初始化
        '''
        super(StoresAndSupermarketsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证商超界面
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SASPC.name_stores_and_spuermarkets_title_st,
                                  SASPC.assert_view_timeout)

    def clickOnStoreOrSupermarket(self):
        '''
        usage: click on the store or supermarket button.
        '''

        tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                        SASPC.xpath_first_store_or_supermarket_st, SASPC.get_text_timeout)

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SASPC.xpath_first_store_or_supermarket_st, SASPC.get_text_timeout)

        return tempText
