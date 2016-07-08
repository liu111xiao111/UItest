#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.store_info_page_configs import StoreInfoPageConfigs


# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage: 门店详情
'''


class StoreInfoPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(StoreInfoPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              StoreInfoPageConfigs.text_store_detail)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_text_contains_android(self.testcase, self.driver, self.logger, keywords)

    def clickOnStoreImageTextDetails(self):
        '''
        usage: click on the store image-text button.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, StoreInfoPageConfigs.xpath_store_image_text_details_button, StoreInfoPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass;
