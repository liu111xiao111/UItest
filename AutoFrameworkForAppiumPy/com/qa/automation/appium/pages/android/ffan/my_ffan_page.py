# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page_configs import MyFfanPageConfigs as MFPC

class MyFfanPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的页面
    '''
    def __init__(self, testcase, driver, logger):
        super(MyFfanPage, self).__init__(testcase, driver, logger)

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
        API().scrollToText(self.driver,
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
        API().scrollToText(self.driver,
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
        API().scrollToText(self.driver,
                           self.logger,
                           MFPC.text_parking_payment)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_parking_payment,
                                 MFPC.verify_view_timeout)
