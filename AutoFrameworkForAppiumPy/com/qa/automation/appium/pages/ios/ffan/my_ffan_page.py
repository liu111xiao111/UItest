# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_page_configs import MyFfanPageConfigs as MFPC


class MyFfanPage(SuperPage):
    '''
    作者 宋波
    首页=>我的(飞凡)
    '''

    def __init__(self, testcase, driver, logger):
        super(MyFfanPage, self).__init__(testcase,
                                         driver,
                                         logger);

    '''
        usage : 进入到应用首页,检查ffan logo
    '''
    def validSelf(self):
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=MFPC.text_my_ffan)

    def clickOnLogin(self):
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, MFPC.text_login)

    def validLoginStatus(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.logger,
                                              self.driver,
                                              MFPC.resource_id_txt_user_nick_name_tv,
                                              seconds=90)

    def clickOnSettings(self):
        API().scroll_to_text(self.driver,
                             self.logger,
                             MFPC.text_settins)
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         MFPC.text_settins)

    def clickOnMyQueue(self):
        '''
        usage : Load "我的排队" page， according to textview in "我的排队", check "我的排队" page whether load correctly.
        '''
        start_x = API().getWidthOfDevice(self.driver, self.logger)/2
        end_x = API().getWidthOfDevice(self.driver, self.logger)/2
        start_y = API().getHeightOfDevice(self.driver, self.logger)/2
        end_y = API().getHeightOfDevice(self.driver, self.logger)/5

        API().scroll(self.driver,
                     self.logger,
                     start_x, start_y, end_x, end_y)

        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_my_queue)

    def clickOnMyTicket(self):
        '''
        usage : Load "我的票券" page， according to textview in "我的票券", check "我的票券" page whether load correctly.
        '''
        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_my_ticket)

    def clickOnMyOrder(self):
        '''
        usage : Load "我的订单" page， according to textview in "我的订单", check "我的订单" page whether load correctly.
        '''
        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_my_order)

    def clickOnMyLike(self):
        '''
        usage : Load "我的喜欢" page， according to textview in "我的喜欢", check "我的喜欢" page whether load correctly.
        '''
        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_my_like)

    def isLoginStatus(self):
        try:
            API().find_view_by_resourceID_Until_android(self.driver,
                                                        self.logger,
                                                        MFPC.resource_id_txt_user_nick_name_tv)
            return True
        except TimeoutError:
            return False

    def clickOnParkingPayment(self):
        '''
        usage : Load "停车交费" page， according to textview in "停车交费", check "停车交费" page whether load correctly.
        '''
        start_x = API().getWidthOfDevice(self.driver, self.logger)/2
        end_x = API().getWidthOfDevice(self.driver, self.logger)/2
        start_y = API().getHeightOfDevice(self.driver, self.logger)/2
        end_y = API().getHeightOfDevice(self.driver, self.logger)/5

        API().scroll(self.driver,
                     self.logger,
                     start_x, start_y, end_x, end_y)

        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_parking_payment)


if __name__ == '__main__':
    pass;
