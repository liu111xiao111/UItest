# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.search_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage: 搜索页面
'''


class SearchPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SearchPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 搜索界面，检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SearchPageConfigs.resource_tv_search_tv, seconds=10);

    '''
        usage ： 输入商家名
    '''

    def inputStoreName(self):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.resource_et_search_input_et,
                                               string=SearchPageConfigs.text_searching_store_name)

    def inputBrandName(self):
        '''
            usage ： 输入品牌名称
        '''
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.resource_et_search_input_et,
                                               string=SearchPageConfigs.text_searching_brand_name)

    def inputGoodsName(self):
        '''
            usage ：输入商品
        '''
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.resource_et_search_input_et,
                                               string=SearchPageConfigs.text_searching_goods_name)

    '''
        usage ： 点击搜索
    '''

    def clickOnSearch(self):
        API().click_view_by_resourceID_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.resource_tv_search_tv);

    '''
        usage : 点击搜索出来的结果list1
    '''

    def clickOnSearchResultFirstItem(self):
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                  xpath=SearchPageConfigs.xpath_search_result_first_item);

    def validSearchResult(self):
        '''
            usage: 验证搜索结果
        '''
        API().assert_view_by_xpath_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                           xpath=SearchPageConfigs.xpath_search_result_first_item)


if __name__ == '__main__':
    pass;
