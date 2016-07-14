# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.le_pay_way_page_configs import LePayWayPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

class LePayWayPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LePayWayPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 判断"选择支付方式"页标题显示是否正确
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=LePayWayPageConfigs.name_choose_pay_way,
                                                      seconds=18);

    def clickOnCancelIcon(self):
        '''
        usage : 点击"X"标示
        '''
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  LePayWayPageConfigs.xpath_cancle_icon)

    def getOrderNumber(self):
        '''
        usage : 取得乐付订单号
        '''
        orderNumber = API().get_view_by_xpath_ios(self.driver, self.logger,
                                                  LePayWayPageConfigs.xpath_order_number).text
        return orderNumber;

if __name__ == '__main__':
    pass;