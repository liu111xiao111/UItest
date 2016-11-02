# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.ios_super_page import IosSuperPage
from com.qa.automation.appium.pages.ios.ffan.shopping_center_page_configs import ShoppingCenterPageConfigs


#
#   购物中心页面
class ShoppingCenterPage(IosSuperPage):

    def __init__(self, testcase, driver, logger):
        super(ShoppingCenterPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    """
        验证购物中心页面navigation bar name是否正确
    """
    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase,
                                                      driver=self.driver,
                                                      logger=self.logger,
                                                      resource_id=ShoppingCenterPageConfigs.name_shopping_center_navigation_bar,
                                                      seconds=90)


if __name__ == '__main__':
    pass;
