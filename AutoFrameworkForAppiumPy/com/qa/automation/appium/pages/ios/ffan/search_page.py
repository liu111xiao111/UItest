# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.search_page_configs import SearchPageConfigs


class SearchPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SearchPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 搜索界面，检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              SearchPageConfigs.resource_id_search_bt,
                                              SearchPageConfigs.assert_view_timeout)

    def inputText(self, text):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.xpath_search_tf,
                                               string=text)

    def inputStoreName(self):
        '''
        usage ： 输入商家名
        '''

        API().input_view_by_xpath_ios(self.driver, self.logger, SearchPageConfigs.xpath_search_tf,
                                      SearchPageConfigs.text_searching_store_name)

    def inputBrandName(self):
        '''
        usage ： 输入品牌名称
        '''

        API().input_view_by_xpath_ios(self.driver, self.logger, SearchPageConfigs.xpath_search_tf,
                                      SearchPageConfigs.text_searching_brand_name)

    def inputGoodsName(self):
        '''
        usage ：输入商品
        '''

        API().input_view_by_xpath_ios(self.driver, self.logger, SearchPageConfigs.xpath_search_tf,
                                      SearchPageConfigs.text_searching_goods_name)

    '''
        usage ： 点击搜索
    '''

    def clickOnSearch(self):
        '''
        usage: click on the search button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SearchPageConfigs.resource_id_search_bt,
                                       SearchPageConfigs.click_on_button_timeout)

    '''
        usage : 点击搜索出来的结果list1
    '''

    def clickOnSearchResultFirstItem(self):
        tempText = API().get_view_by_xpath_android(self.testcase, self.driver, self.logger,
                                                SearchPageConfigs.xpath_specific_store_tv).text
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  SearchPageConfigs.xpath_search_result_first_item_tv,
                                  SearchPageConfigs.click_on_button_timeout)

        return tempText

    def clickOnMovie(self):
        '''
        usage: click on the movie button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, SearchPageConfigs.text_movie_button, SearchPageConfigs.click_on_button_timeout)

    def clickOnSpecificMovie(self):
        '''
        usage: click on the specific movie button
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, SearchPageConfigs.xpath_specific_movie_st, SearchPageConfigs.click_on_button_timeout)

    def validSearchResult(self, textContains="default", xpath="default"):
        '''
            usage: 验证搜索结果
        '''

        API().assert_view_by_text_contains_according_to_xpath_until_android(self.testcase, self.driver, self.logger, textContains, xpath, SearchPageConfigs.assert_view_timeout)

    def inputKeywords(self, keywords):
        '''
        usage: input keywords.
        '''

        API().input_view_by_xpath_ios(self.driver, self.logger, SearchPageConfigs.xpath_search_tf, keywords)

    def clickOnSpecificSquare(self):
        '''
        usage: click on the specific square button
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                       SearchPageConfigs.xpath_specific_square_st,
                                       SearchPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass;
