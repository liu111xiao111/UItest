# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_active_details_page_configs import SalesPromotionActiveDetailsPageConfigs

class SalesPromotionActiveDetailsPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionActiveDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self, itemtext="default"):
        '''
            usage : "活动详情" 页加载是否正确
        '''
        activeName = API().get_view_by_xpath_ios(self.driver, self.logger,
                                    SalesPromotionActiveDetailsPageConfigs.xpath_active_details_title_tv).text
        API().assert_equal(self.testcase, self.driver, self.logger, itemtext, activeName)


if __name__ == '__main__':
    pass;