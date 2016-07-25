# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.goods_details_page_configs import GoodsDetailsPageConfigs


class GoodsDetailsPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>爱购物=>商品详情
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(GoodsDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              GoodsDetailsPageConfigs.resource_id_reource_goods_details_title_st,
                                              GoodsDetailsPageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print ("KEYWORDS: %s" % keywords)

        API().assert_view_by_text_contains_according_to_xpath_until_android(self.testcase, self.driver,
                                                                            self.logger, keywords,
                                                                            GoodsDetailsPageConfigs.xpath_commodity_name_st,
                                                                            GoodsDetailsPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
