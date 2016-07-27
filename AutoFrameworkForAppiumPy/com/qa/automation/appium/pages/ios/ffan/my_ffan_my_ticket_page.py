# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_ticket_page_configs import MyFfanMyTicketPageConfigs


class MyFfanMyTicketPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的票券
    '''

    def __init__(self, testcase, driver, logger):
        super(MyFfanMyTicketPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self, couponNumber, myCouponNumber):
        '''
        usage : 判断"我的票券"券码显示是否正确
        '''
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=couponNumber,
                          expectText=myCouponNumber)

    def clickOnTicketUnused(self):
        '''
        usage : Click "未使用" in my ticket page， and load "未使用" tab correctly.
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_unused)

    def clickOnTicketUsed(self):
        '''
        usage : Click "已使用" in my ticket page， and load "已使用" tab correctly.
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_used)

    def clickOnTicketOutOfDate(self):
        '''
        usage : Click "已过期" in my ticket page， and load "已过期" tab correctly.
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_out_of_date)

    def clickOnReturnRefund(self):
        '''
        usage : Click "退货退款" in my ticket page， and load "退货退款" tab correctly.
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_return_refund)

    def validSelfUsed(self):
        '''
        usage : Load "已使用" tab correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyTicketPageConfigs.text_ticket_used, seconds=10);

    def validSelfOutOfDate(self):
        '''
        usage : Load "已过期" tab correctly.
        '''

        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyTicketPageConfigs.text_ticket_out_of_date, seconds=10);

    def validSelfReturnRefund(self):
        '''
        usage : Load "退货退款" tab correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyTicketPageConfigs.text_ticket_return_refund, seconds=10);

    def getTicketNo(self):
        '''
        usage : Get ticket number.
        '''
        ticketNumber = API().getTextByXpath(self.testcase,
                                           self.driver,
                                           self.logger,
                                           MyFfanMyTicketPageConfigs.xpath_my_ticket_no_tv)
        return ticketNumber[3:];

    def validSelfTicketNo(self, ticketName="default"):
        '''
        usage : Check ticket name correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=ticketName, seconds=10);

    def validCouponCode(self, couponCode="default"):
        '''
        usage: verify whether the coupon is correct.
        '''

        API().assert_view_by_text_contains_according_to_xpath_until_android(self.testcase, self.driver,
                                                                            self.logger, couponCode,
                                                                            MyFfanMyTicketPageConfigs.xpath_coupon_code_button,
                                                                            MyFfanMyTicketPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass;
