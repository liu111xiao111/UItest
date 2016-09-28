# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_ffan_my_ticket_page_configs import MyFfanMyTicketPageConfigs as MMTPC


class MyFfanMyTicketPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的票券
    '''
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyTicketPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 判断"我的票券"券码显示是否正确
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MMTPC.resource_id_tv_my_ticket_tv,
                                        MMTPC.assert_view_timeout)

    def clickOnTicketUnused(self):
        '''
        usage : 点击未使用
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMTPC.text_ticket_unused,
                                 MMTPC.click_view_timeout)

    def clickOnTicketUsed(self):
        '''
        usage : 点击已使用
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMTPC.text_ticket_used,
                                 MMTPC.click_view_timeout)

    def clickOnTicketOutOfDate(self):
        '''
        usage : 点击已过期
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMTPC.text_ticket_out_of_date,
                                 MMTPC.click_view_timeout)

    def clickOnReturnRefund(self):
        '''
        usage : 点击退货退款
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMTPC.text_ticket_return_refund,
                                 MMTPC.click_view_timeout)

    def validSelfUsed(self):
        '''
        usage : 验证已使用正确
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMTPC.text_ticket_used,
                                  MMTPC.assert_view_timeout)

    def validSelfOutOfDate(self):
        '''
        usage : 验证已过期正确
        '''

        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMTPC.text_ticket_out_of_date,
                                  MMTPC.assert_view_timeout)

    def validSelfReturnRefund(self):
        '''
        usage : 验证退货退款正确
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMTPC.text_ticket_return_refund,
                                  MMTPC.assert_view_timeout)

    def getTicketNo(self):
        '''
        usage : 获取券数
        '''
        ticketNumber = API().getTextByResourceId(self.testCase,
                                                 self.driver,
                                                 self.logger,
                                                 MMTPC.resource_id_tv_my_ticket_no_tv,
                                                 MMTPC.assert_view_timeout)
        return ticketNumber[3:];

    def validSelfTicketName(self, ticketName="default"):
        '''
        usage : 验证票券名字
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  ticketName,
                                  MMTPC.assert_view_timeout)

    def validCouponCode(self, couponCode="default"):
        '''
        usage: 验证优惠是否有效
        '''
        text = API().getTextByXpath(self.testCase,
                                    self.driver,
                                    self.logger,
                                    MMTPC.xpath_coupon_code_button,
                                    MMTPC.assert_view_timeout)
        API().assertGreaterEqual(self.testCase,
                                 self.logger,
                                 text,
                                 couponCode)
