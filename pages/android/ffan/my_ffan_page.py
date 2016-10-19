# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_ffan_page_configs import MyFfanPageConfigs as MFPC

class MyFfanPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的页面
    '''
    def validSelf(self):
        '''
        usage : 进入到应用首页,检查ffan logo
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MFPC.text_member_card_bag,
                                  MFPC.verify_view_timeout)
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MFPC.resource_id_txt_user_nick_name_tv,
                                        MFPC.verify_view_timeout)

    def clickOnLogin(self):
        '''
        usage: 点击登录按钮
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MFPC.resource_id_tv_login_tv,
                                       MFPC.click_view_timeout)

    def validLoginStatus(self):
        '''
        usage： 验证登录状态
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.logger,
                                        self.driver,
                                        MFPC.resource_id_txt_user_nick_name_tv,
                                        90)

    def clickOnSettings(self):
        '''
        usage： 点击设置
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           MFPC.text_settins)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_settins,
                                 MFPC.verify_view_timeout)

    def clickOnMyQueue(self):
        '''
        usage : 点击我的排队
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           MFPC.text_my_queue)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_my_queue,
                                 MFPC.verify_view_timeout)

    def clickOnMyTicket(self):
        '''
        usage : 点击我的票券
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_my_ticket,
                                 MFPC.verify_view_timeout)

    def clickOnMyOrder(self):
        '''
        usage : 点击我的订单
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_my_order,
                                 MFPC.click_view_timeout)

    def clickOnToBePaid(self):
        '''
        usage : 点击我的订单待付款
        '''
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(3):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)

        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.xpath_to_be_paid,
                                 MFPC.click_view_timeout)

    def validSelfToBePaid(self):
        '''
        usage : 进入待付款页面，判断显示是否正确
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MFPC.text_to_be_paid,
                                  MFPC.verify_view_timeout)

    def clickOnUse(self):
        '''
        usage : 点击我的订单可使用
        '''
        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.xpath_use,
                                 MFPC.click_view_timeout)

    def validSelfUse(self):
        '''
        usage : 进入可使用页面，判断显示是否正确
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MFPC.text_use,
                                  MFPC.verify_view_timeout)
        network = API().validElementByXpath(self.driver,
                                            self.logger,
                                            MFPC.text_use,
                                            MFPC.verify_view_timeout)
        if not network:
            API().assertTrue(self.testcase, self.logger, False)

    def clickOnComments(self):
        '''
        usage : 点击我的订单我的点评
        '''
        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.xpath_comments,
                                 MFPC.click_view_timeout)

    def validSelfCommets(self):
        '''
        usage : 进入我的点评页面，判断显示是否正确
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MFPC.text_comments,
                                  MFPC.verify_view_timeout)

    def clickOnReturnRefund(self):
        '''
        usage : 点击我的订单退货退款
        '''
        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.xpath_return_refund,
                                 MFPC.click_view_timeout)

    def validSelfReturnRefund(self):
        '''
        usage : 进入退货退款页面，判断显示是否正确
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MFPC.text_return_refund,
                                  MFPC.verify_view_timeout)

    def clickOnMyLike(self):
        '''
        usage : 点击我的喜欢
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_my_like,
                                 MFPC.verify_view_timeout)

    def isLoginStatus(self):
        '''
        usage: 返回登录状态
        '''
        return API().validElementByResourceId(self.driver,
                                       self.logger,
                                       MFPC.resource_id_txt_user_nick_name_tv,
                                       MFPC.verify_view_timeout)

    def clickOnParkingPayment(self):
        '''
        usage : 点击停车缴费
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           MFPC.text_parking_payment)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_parking_payment,
                                 MFPC.verify_view_timeout)

    def getTicketNumber(self):
        '''
        usage : 获取我的票券数量
        '''
        ticketNumber = API().getTextByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.resource_id_txt_ticket_number_tv,
                                 MFPC.verify_view_timeout)
        return ticketNumber

    def clickOnMyBill(self):
        '''
        usage : 点击我的零花钱
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_my_bill,
                                 MFPC.click_view_timeout)
