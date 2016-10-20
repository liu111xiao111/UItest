# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.search_result_store_page_configs import SearchResultStorePageConfigs


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
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SearchResultStorePageConfigs.text_tongzhou,
                                  SearchResultStorePageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger,
                                          keywords, SearchResultStorePageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass;
