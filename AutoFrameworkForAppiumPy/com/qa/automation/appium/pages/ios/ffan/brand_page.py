# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.brand_page_configs import BrandPageConfigs


#   电影选择页面,入口:首页 -> 品牌
class BrandPage(SuperPage):

    def __init__(self, test_case, driver, logger):
        super(BrandPage, self).__init__(testcase=test_case, driver=driver, logger=logger);

    """
        验证品牌页面navigation bar name是否正确
    """
    def validSelf(self):
        navigation_bar = API().find_view_by_class_name_both(driver=self.driver,logger=self.logger,
                                                            className=BrandPageConfigs.class_NavigationBar)
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           expect_text=BrandPageConfigs.name_brand_navigation_bar,
                           actual_text=navigation_bar.get_attribute("name"))

if __name__ == '__main__':
    pass;
