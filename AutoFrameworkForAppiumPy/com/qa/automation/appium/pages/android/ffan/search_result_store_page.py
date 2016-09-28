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
        '''API().assertElementByContainsText(self.testcase, self.driver, self.logger,
                                  SPC.text_store_detail,
                                  SPC.assert_view_timeout)'''
        API().assertElementByText(self.testcase, self.driver, self.logger,
                                  SPC.text_store_details,
                                  SPC.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementsByContentDescs(self.testcase, self.driver, self.logger,
                                  keywords,
                                  SPC.assert_view_timeout)

    def validHotWords(self, length = 0):
        '''
        usage: 验证热词检索列表长度及检索出的条目包含热词内容
        '''
        API().assertGreaterEqual(self.testcase, self.logger, length, SPC.expectLenth)
        API().assertElementsByContainsTexts(self.testcase, self.driver, self.logger,
                                            SPC.text_shopping_mall, SPC.assert_view_timeout)

    def getShoppingMallListItemTitle(self):
        '''
        usage: 取得检索热词名称
        '''
        item = API().getTextByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPC.resource_id_first_item,
                                       SPC.get_view_timeout)
        return item

    def clickOnShoppingMallItem(self):
        '''
        usage: 点击热词“百货”检索后的第一条项目
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPC.resource_id_first_item,
                                       SPC.click_on_button_timeout)
