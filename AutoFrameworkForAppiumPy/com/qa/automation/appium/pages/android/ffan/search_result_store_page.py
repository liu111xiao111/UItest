# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.search_page_configs import SearchPageConfigs as SPC


class SearchResultStorePage(SuperPage):
    '''
    作者 宋波
    首页=>搜索页=>搜索结果店详情
    '''
    def __init__(self, testcase, driver, logger):
        super(SearchResultStorePage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 检查是否加载出来
        '''
        API().assertElementByContainsText(self.testcase, self.driver, self.logger,
                                  SPC.text_store_detail,
                                  SPC.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementByContentDesc(self.testcase, self.driver, self.logger,
                                  keywords,
                                  SPC.assert_view_timeout)
