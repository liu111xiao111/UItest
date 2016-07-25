# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_details_page_configs import LePayDetailsPageConfigs


class LePayDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付=>输入乐付消费金额页
    '''

    def __init__(self, testcase, driver, logger):
        super(LePayDetailsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 判断乐付买单输入金额页是否存在“确认购买”按钮
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=LePayDetailsPageConfigs.name_pay,
                                                      seconds=18);

    def inputMoney(self):
        '''
        usage : 输入消费金额
        '''
        API().input_view_by_xpath_ios(self.driver, self.logger, LePayDetailsPageConfigs.xpath_total_money,
                                      LePayDetailsPageConfigs.total_money)

    def clickOnPay(self):
        '''
        usage : Click "确认购买"
        '''
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  LePayDetailsPageConfigs.xpath_pay)


if __name__ == '__main__':
    pass;