# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.feifan_card_integral_page_configs import FeiFanCardIntegralPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

class FeiFanCardIntegralPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardIntegralPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Check "积分主页" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=FeiFanCardIntegralPageConfigs.resource_id_tv_integral_tv,
                                                      seconds=10)
        # API().assert_view_by_resourceID_Until_android(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = FeiFanCardIntegralPageConfigs.resource_id_tv_myIntegral_tv, seconds = 10)


if __name__ == '__main__':
    pass;