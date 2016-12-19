# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.search_page_configs import SearchPageConfigs as SPC
from pages.logger import logger


class Ranking(object):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4


class Orientation(object):
    LEFT = "left"
    RIGHT = "right"


class SearchPage(SuperPage):
    '''
    作者 陈诚
    usage: 搜索页面
    '''
    def __init__(self, testcase, driver, logger):
        super(SearchPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 搜索页面，检查是否加载出来
        '''
        logger.info("Check 搜索页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPC.resource_tv_search_tv,
                                        10)
        logger.info("Check 搜索页面 end")

    def inputText(self, text):
        '''
        usage : 输入文本值
        '''
        logger.info("Input 文本 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      text,
                                      10)
        logger.info("Input 文本 end")

    def inputStoreName(self):
        '''
        usage : 输入商家名
        '''
        logger.info("Input 门店名称 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      SPC.text_searching_store_name,
                                      10)
        #API().screenShot(self.driver, "souSuo")
        logger.info("Input 门店名称 end")

    def inputGuangChangStoreName(self):
        '''
        usage : 输入商家名(广场找店)
        '''
        logger.info("Input 门店名称 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      SPC.text_searching_square_store_name,
                                      10)
        #API().screenShot(self.driver, "souSuo")
        logger.info("Input 门店名称 end")

    def inputBrandName(self):
        '''
        usage ： 输入品牌名称
        '''
        logger.info("Input 品牌名称 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      SPC.text_searching_brand_name,
                                      10)
        logger.info("Input 品牌名称 end")

    def inputGoodsName(self):
        '''
        usage ：输入商品
        '''
        logger.info("Input 商品名称 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      SPC.resource_et_search_input_et,
                                      SPC.text_searching_goods_name,
                                      10)
        logger.info("Input 商品名称 end")

    def clickOnSearch(self):
        '''
        usage ： 点击搜索
        '''
        logger.info("Click 搜索 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPC.resource_tv_search_tv,
                                       90)
        logger.info("Click 搜索 end")

    def clickOnSearchResultFirstItem(self):
        '''
        usage : 点击搜索出来的结果list1
        '''
        logger.info("Click 搜索列表第一项 begin")
#         API().getTextByResourceId(self.testcase,
#                                   self.driver,
#                                   self.logger,
#                                   SPC.resource_id_specific_store_button,
#                                   90)
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPC.xpath_search_result_first_item,
                                  90)

    def clickOnFindStoreFirstItem(self):
        '''
        usage : 点击搜索出来的结果list1
        '''
        logger.info("Click 找店搜索列表第一项 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPC.xpath_find_store_first_item,
                                  90)

        #return tempText
        logger.info("Click 搜索列表第一项 end")

    def clickOnMovie(self):
        '''
        usage: 点击电影
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPC.text_movie_button,
                                 SPC.click_on_button_timeout)

    def clickOnShoppingMall(self):
        '''
        usage: 点击百货
        '''
        logger.info("Click 百货 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPC.text_shopping_mall,
                                 SPC.click_on_button_timeout)
        logger.info("Click 百货 end")

    def getHotWordListLength(self):
        '''
        usage: 取得检索出的百货列表长度
        '''
        logger.info("Get 检索出的列表长度 begin")
        elements = API().getElementsByResourceId(self.testcase,
                                                 self.driver,
                                                 self.logger,
                                                 SPC.resource_id_first_item,
                                                 SPC.get_view_timeout)
        logger.info("Get 检索出的列表长度 end")
        return len(elements)

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
        logger.info("Check 搜索结果 begin")
        text = API().getTextByXpath(self.testcase,
                             self.driver,
                             self.logger,
                             xpath,
                             SPC.assert_view_timeout)
        API().assertTrue(self.testcase,
                         self.logger,
                         textContains in text)
        logger.info("Check 搜索结果 end")

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

    def validHotWordModule(self, keyword=None, ranking=Ranking.FIRST):
        '''
        usage：验证热词模块显示正常。
        '''

        if keyword is None:
            API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                            SPC.resource_id_hot_word_module_tv, SPC.valid_view_timeout)
        else:
            API().assertFalse(self.testcase, self.logger, keyword == self.getHotWordModule(ranking))

    def getHotWordModule(self, ranking=Ranking.FIRST):
        '''
        usage: 获取热词。
        '''

        return API().getTextByXpath(self.testcase, self.driver, self.logger,
                                    SPC.xpath_hot_word_module_tv % ranking, SPC.get_view_timeout)

    def slideHotWordModule(self, keyword, ranking=Ranking.FIRST, orientation=Orientation.RIGHT):
        '''
        usage: 滑行热词搜索模块。
        '''

        if "left" == orientation:
            self.scrollAsScreenPercent(0.2, 0.2, 0.8, 0.2)
        elif "right" == orientation:
            self.scrollAsScreenPercent(0.8, 0.2, 0.2, 0.2)

        API().waitBySeconds()
        API().assertFalse(self.testcase, self.logger, keyword == self.getHotWordModule())
