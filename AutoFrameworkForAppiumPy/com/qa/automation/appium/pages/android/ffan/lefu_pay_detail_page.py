# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.lefu_pay_detail_page_configs import LefuPayDetailPageConfigs


class LefuPayDetailPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LefuPayDetailPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Click "乐付买单" in square page, and load "乐付买单" correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=LefuPayDetailPageConfigs.resource_id_store_title,
                                                      seconds=18);

    def inputMoney(self):
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id=LefuPayDetailPageConfigs.resource_id_total_money,
                                               string=LefuPayDetailPageConfigs.total_money
                                               );

    def clickOnPay(self):
        '''
        usage : Click "确认购买"
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=LefuPayDetailPageConfigs.resource_id_pay);


if __name__ == '__main__':
    pass;