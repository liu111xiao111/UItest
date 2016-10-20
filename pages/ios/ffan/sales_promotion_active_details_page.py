# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.sales_promotion_active_details_page_configs import SalesPromotionActiveDetailsPageConfigs

class SalesPromotionActiveDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动=>活动详情页
    '''

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionActiveDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self, itemtext="default"):
        '''
            usage : "活动详情" 页加载是否正确
        '''
        activeName = API().getTextByXpath(self.testcase,
                                          self.driver,
                                          self.logger,
                                          SalesPromotionActiveDetailsPageConfigs.xpath_active_details_title_tv)
        API().assertEqual(self.testcase, self.logger, itemtext, activeName)


if __name__ == '__main__':
    pass;