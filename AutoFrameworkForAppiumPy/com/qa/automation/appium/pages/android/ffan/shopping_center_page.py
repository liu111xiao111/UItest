# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.shopping_center_page_configs import ShoppingCenterPageConfigs


#   单个购物中心、广场页面
class ShoppingCenterPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(ShoppingCenterPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage :
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase,
                                                      driver=self.driver,
                                                      logger=self.logger,
                                                      resource_id=ShoppingCenterPageConfigs.resource_id_image_zone_logo_iv,
                                                      seconds=90)


if __name__ == '__main__':
    pass;
