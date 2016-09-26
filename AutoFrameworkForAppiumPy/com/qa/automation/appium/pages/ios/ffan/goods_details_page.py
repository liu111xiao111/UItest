# -*- coding:utf-8 -*-

import logging

from com.qa.automation.appium.api.api_new import API
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

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  GoodsDetailsPageConfigs.resource_id_reource_goods_details_title_st,
                                  GoodsDetailsPageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        logging.info("KEYWORDS: %s" % keywords)

        tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                        GoodsDetailsPageConfigs.xpath_commodity_name_st,
                                        GoodsDetailsPageConfigs.assert_view_timeout)
        #self.logger.d("window size keywords= s%" + keywords);
        #self.logger.d("window size tempText= s%" + tempText);
        API().assertTrue(self.testcase, self.logger, keywords in tempText)


if __name__ == '__main__':
    pass
