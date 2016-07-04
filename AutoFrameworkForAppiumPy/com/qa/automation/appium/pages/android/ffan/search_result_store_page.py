# -*- coding: utf-8 -*-

import os, sys
from time import sleep
import unittest

from appium import webdriver

from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.common.super_page import *
from com.qa.automation.appium.pages.android.ffan.search_page_configs import SearchPageConfigs


# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage: 门店详情
'''


class SearchResultStorePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SearchResultStorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=SearchPageConfigs.text_store_detail);

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger,
											keywords, SearchPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass;
