# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.search_result_store_page_configs import SearchResultStorePageConfigs
from pages.logger import logger

class SearchResultStorePage(SuperPage):
    '''
    作者 宋波
    首页=>搜索页=>搜索结果店详情
    '''

    def __init__(self, testcase, driver, logger):
        super(SearchResultStorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
    usage : 检查是否加载出来
    '''
    def validSelf(self):
        logger.info("Check 搜索结果 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SearchResultStorePageConfigs.text_tongzhou,
                                  SearchResultStorePageConfigs.assert_view_timeout)
        logger.info("Check 搜索结果 end")
        API().screenShot(self.driver, "souSuoJieGuo")

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''
        logger.info("Input " + keywords + " begin")
        API().assert_view_by_text_android(self.testcase, self.driver, self.logger,
                                          keywords, SearchResultStorePageConfigs.assert_view_timeout)
        logger.info("Input " + keywords + " end")
        API().screenShot(self.driver, "guanJianZi")

if __name__ == '__main__':
    pass;
