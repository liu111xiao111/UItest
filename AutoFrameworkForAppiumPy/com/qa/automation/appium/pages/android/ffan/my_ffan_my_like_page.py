# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_like_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyFfanMyLikePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyLikePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "我的喜欢" page， according to textview in "我的喜欢", check "我的喜欢" page whether load correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=MyFfanMyLikePageConfigs.resource_id_tv_my_like_tv)

    def clickOnLikeGoods(self):
        '''
        usage : Click "商品" in my order page， and load "商品" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyLikePageConfigs.text_like_goods)

    def clickOnLikeDissertation(self):
        '''
        usage : Click "专题" in my order page， and load "专题" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyLikePageConfigs.text_like_dissertation)

    def clickOnLikeBrand(self):
        '''
        usage : Click "品牌" in my order page， and load "品牌" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyLikePageConfigs.text_like_brand)

    def validSelfDissertation(self):
        '''
        usage : Load "专题" correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyLikePageConfigs.text_like_dissertation, seconds=10);

    def validSelfBrand(self):
        '''
        usage : Load "品牌" correctly.
        '''

        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyLikePageConfigs.text_like_brand, seconds=10);


if __name__ == '__main__':
    pass;