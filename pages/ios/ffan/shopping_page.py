# -*- coding: utf-8 -*-

from pages.ios.ffan.shopping_page_configs import ShoppingPageConfigs
from api.api import API
from pages.ios.common.superPage import SuperPage


#   首页点击 购物
class ShoppingPage(SuperPage):

    def __init__(self, testcase, driver, logger):
        super(ShoppingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),expect_text=ShoppingPageConfigs.name_shopping_navigation_bar)


if __name__ == '__main__':
    pass;
