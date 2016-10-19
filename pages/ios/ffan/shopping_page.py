# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.shopping_page_configs import ShoppingPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.ios_super_page import IosSuperPage


#   首页点击 购物
class ShoppingPage(IosSuperPage):

    def __init__(self, testcase, driver, logger):
        super(ShoppingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),expect_text=ShoppingPageConfigs.name_shopping_navigation_bar)


if __name__ == '__main__':
    pass;
