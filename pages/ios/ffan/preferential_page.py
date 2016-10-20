# -*- coding: utf-8 -*-

from pages.ios.ffan.preferential_page_configs import PreferentialPageConfigs
from api.api import API
from pages.ios.common.superPage import SuperPage


#   首页 优惠
class PreferentialPage(SuperPage):

    def __init__(self, testcase, driver, logger):
        super(PreferentialPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),
                           expect_text=PreferentialPageConfigs.name_navagation_bar)


if __name__ == '__main__':
    pass;
