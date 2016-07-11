# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.le_pay_page_configs import LePayPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.ios_super_page import IosSuperPage


#   首页点击 乐付
class LePayPage(IosSuperPage):

    def __init__(self, testcase, driver, logger):
        super(LePayPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),expect_text=LePayPageConfigs.name_le_pay_navigation_bar)


if __name__ == '__main__':
    pass;
