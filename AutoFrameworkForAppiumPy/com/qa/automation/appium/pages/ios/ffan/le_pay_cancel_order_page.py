# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.le_pay_cancel_order_configs import LePayCancelOrderPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class LePayCancelOrderPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LePayCancelOrderPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def clickOnConfirmBtn(self):
        '''
            usage : 点击 "好" button
        '''
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                  resource_id = LePayCancelOrderPageConfigs.name_confirm_button)


if __name__ == '__main__':
    pass;