# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.preferential_page_configs import PreferentialPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.ios_super_page import IosSuperPage


#   首页 优惠
class PreferentialPage(IosSuperPage):

    def __init__(self, testcase, driver, logger):
        super(PreferentialPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),
                           expect_text=PreferentialPageConfigs.name_navagation_bar)


if __name__ == '__main__':
    pass;
