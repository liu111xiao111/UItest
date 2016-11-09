# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.search_page_configs import SearchPageConfigs
from pages.logger import logger

class SearchPage(SuperPage):
    '''
    作者 宋波
    首页=>搜索页
    '''

    def __init__(self, testcase, driver, logger):
        super(SearchPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 搜索界面，检查是否加载出来
    '''

    def validSelf(self):
        logger.info("Check 搜索界面 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SearchPageConfigs.resource_id_search_bt,
                                  SearchPageConfigs.assert_view_timeout)
        API().screenShot(self.driver, "sousuojiemian")
        logger.info("Check 搜索界面 end")

    def inputText(self, text):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=SearchPageConfigs.xpath_search_tf,
                                               string=text)

    def inputStoreName(self):
        '''
        usage ： 输入商家名
        '''

        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 SearchPageConfigs.xpath_search_tf,
                                 SearchPageConfigs.text_searching_store_name,
                                 SearchPageConfigs.input_timeout)

    def inputBrandName(self):
        '''
        usage ： 输入品牌名称
        '''
        logger.info("Input adidas begin")
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 SearchPageConfigs.xpath_search_tf,
                                 SearchPageConfigs.text_searching_brand_name,
                                 SearchPageConfigs.input_timeout)
        API().screenShot(self.driver,"shuRuPinPai")
        logger.info("Input adidas end")

    def inputGoodsName(self):
        '''
        usage ：输入商品
        '''
        logger.info("Input MU8600 begin")
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 SearchPageConfigs.xpath_search_tf,
                                 SearchPageConfigs.text_searching_goods_name,
                                 SearchPageConfigs.input_timeout)
        API().screenShot(self.driver, "shuRuShangPin")
        logger.info("Input MU8600 end")

    '''
        usage ： 点击搜索
    '''

    def clickOnSearch(self):
        '''
        usage: click on the search button.
        '''
        logger.info("Click 搜索按钮 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SearchPageConfigs.name_search_bt,
                                 SearchPageConfigs.click_on_button_timeout)
        logger.info("Click 搜索按钮 end")

    '''
        usage : 点击搜索出来的结果list1
    '''

    def clickOnSearchResultFirstItem(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SearchPageConfigs.xpath_search_result_first_item_tv,
                                  SearchPageConfigs.click_on_button_timeout)

    def clickOnMovie(self):
        '''
        usage: click on the movie button
        '''
        logger.info("Click 电影 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SearchPageConfigs.text_movie_button,
                                 SearchPageConfigs.click_on_button_timeout)
        API().screenShot(self.driver, "dianYing")
        logger.info("Click 电影 end")

    def clickOnSpecificMovie(self):
        '''
        usage: click on the specific movie button
        '''
        logger.info("Click 某一个电影 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SearchPageConfigs.xpath_specific_movie_st,
                                  SearchPageConfigs.click_on_button_timeout)

        logger.info("Click 某一个电影 end")

    def validSearchResult(self, textContains="default", xpath="default"):
        '''
            usage: 验证搜索结果
        '''
        logger.info("Check 搜索结果页面 begin")
        tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                        xpath, SearchPageConfigs.get_timeout)
        API().assertTrue(self.testcase, self.logger, textContains in tempText)
        API().screenShot(self.driver,"souSuoJieGuo")
        logger.info("Check 搜索结果页面 end")

    def inputKeywords(self, keywords):
        '''
        usage: input keywords.
        '''

        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 SearchPageConfigs.xpath_search_tf, keywords,
                                 SearchPageConfigs.input_timeout)

    def clickOnSpecificSquare(self):
        '''
        usage: click on the specific square button
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SearchPageConfigs.xpath_specific_square_st,
                                  SearchPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass;
