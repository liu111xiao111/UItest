#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Title: shopping_mall_page.py
Package: com.qa.automation.appium.pages.android.ffan
Description: This is shopping mall page operation class.
Company: Neusoft
All rights Reserved, Designed By Zhaosheng Liu
@copyright: Copyright(C) 2016-2017
@author: Zhaosheng Liu
@date Jun 17, 2016 05:37:35 PM
Modification  History:
Date                Author                Version                Description
Jun 17, 2016        liuzhsh               V0.0.0.1               New file
Why & What is modified: TODO
'''

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.shopping_mall_page_configs import ShoppingMallPageConfigs

class ShoppingMallPage(SuperPage):
    '''
    This is shopping mall page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(ShoppingMallPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, ShoppingMallPageConfigs.resource_id_shopping_mall_title, ShoppingMallPageConfigs.assert_view_timeout)

    def clickOnTotal(self):
        '''
        usage: click total button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, ShoppingMallPageConfigs.resource_id_total_button, ShoppingMallPageConfigs.click_on_button_timeout)

    def clickOnSpecificShoppingMall(self):
        '''
        usage: click specific shopping mall button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, ShoppingMallPageConfigs.resource_id_specific_shopping_mall_button, ShoppingMallPageConfigs.click_on_button_timeout)

    def clickOnBeijinTongzouMall(self):
        '''
        usage: click "北京通州万达广场"
        '''

        API().scroll_to_text(self.driver, self.logger, ShoppingMallPageConfigs.text_beijing_tongzou_mall)
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger, text=ShoppingMallPageConfigs.text_beijing_tongzou_mall);

if __name__ == '__main__':
    pass
