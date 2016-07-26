# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.search_page_configs import SearchPageConfigs as SPC


class SearchPage(SuperPage):
    '''
    作者 陈诚
    usage: 搜索页面
    '''
    def __init__(self, testcase, driver, logger):
        super(SearchPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 搜索界面，检查是否加载出来
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPC.resource_tv_search_tv,
                                        10)

    def inputText(self, text):
        '''
        usage : 输入文本值
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      text,
                                      10)

    def inputStoreName(self):
        '''
        usage : 输入商家名
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      SPC.text_searching_store_name,
                                      10)

    def inputBrandName(self):
        '''
        usage ： 输入品牌名称
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      SPC.text_searching_brand_name,
                                      10)

    def inputGoodsName(self):
        '''
        usage ：输入商品
        '''
        API().inputStringByResourceId(self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      SPC.text_searching_goods_name,
                                      10)

    def clickOnSearch(self):
        '''
        usage ： 点击搜索
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPC.resource_tv_search_tv,
                                       10)

    def clickOnSearchResultFirstItem(self):
        '''
        usage : 点击搜索出来的结果list1
        '''
        tempText = API().getTextByResourceId(self.testcase,
                                             self.driver,
                                             self.logger,
                                             SPC.resource_id_specific_store_button,
                                             10)
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPC.xpath_search_result_first_item,
                                  10)

        return tempText

    def clickOnMovie(self):
        '''
        usage: 点击电影
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPC.text_movie_button,
                                 SPC.click_on_button_timeout)

    def clickOnSpecificMovie(self):
        '''
        usage: 点击特别推荐电影
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPC.resource_id_specific_movie_button,
                                       SPC.click_on_button_timeout)

    def validSearchResult(self, textContains="default", xpath="default"):
        '''
        usage: 验证搜索结果
        '''
        text = API().getTextByXpath(self.testcase,
                             self.driver,
                             self.logger,
                             xpath,
                             SPC.assert_view_timeout)
        API().assertGreaterEqual(self.testcase,
                                 self.logger,
                                 text,
                                 textContains)

    def inputKeywords(self, keywords):
        '''
        usage: 输入关键值
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      keywords,
                                      10)

    def clickOnSpecificSquare(self):
        '''
        usage: 点击推荐广场
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPC.resource_id_specific_square_button,
                                       SPC.click_on_button_timeout)
