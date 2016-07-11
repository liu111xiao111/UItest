# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.search_page_configs import SearchPageConfigs


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



    def inputText(self, text):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.resource_et_search_input_et,
                                               string=text)

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
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.resource_tv_search_tv);

    '''
        usage : 点击搜索出来的结果list1
    '''

    def clickOnSearchResultFirstItem(self):
        tempText = API().get_view_by_resourceID(self.driver, self.logger, SearchPageConfigs.resource_id_specific_store_button).text
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.logger, xpath=SearchPageConfigs.xpath_search_result_first_item);

        return tempText

    def clickOnMovie(self):
        '''
        usage: click on the movie button
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, SearchPageConfigs.text_movie_button, SearchPageConfigs.click_on_button_timeout)

    def clickOnSpecificMovie(self):
        '''
        usage: click on the specific movie button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, SearchPageConfigs.resource_id_specific_movie_button, SearchPageConfigs.click_on_button_timeout)

    def validSearchResult(self, textContains="default", xpath="default"):
        '''
            usage: 验证搜索结果
        '''

        API().assert_view_by_text_contains_according_to_xpath_until_android(self.testcase, self.driver, self.logger, textContains, xpath, SearchPageConfigs.assert_view_timeout)

    def inputKeywords(self, keywords):
        '''
        usage: input keywords.
        '''

        API().input_view_by_resourceID_android(self.driver, self.logger,
												SearchPageConfigs.resource_et_search_input_et,
												keywords)

    def clickOnSpecificSquare(self):
        '''
        usage: click on the specific square button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
										SearchPageConfigs.resource_id_specific_square_button,
										SearchPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass;
