# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.my_ffan_page_configs import MyFfanPageConfigs as MFPC
from pages.logger import logger

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
        logger.info("Check 我的飞凡页面 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=MFPC.text_my_ffan)
        logger.info("Check 我的飞凡页面 end")
        API().screenShot(self.driver, "myFeiFan")

    def clickOnLogin(self):
        logger.info("Click 注册 begin")
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, MFPC.text_login)
        logger.info("Click 注册 end")


    def validLoginStatus(self):
        logger.info("Check 注册 begin")
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.logger,
                                              self.driver,
                                              MFPC.resource_id_txt_user_nick_name_tv,
                                              seconds=90)
        logger.info("Check 注册 begin")
        API().screenShot(self.driver, "login")

    def clickOnSettings(self):
        logger.info("Click 设置 begin")
        API().scroll_to_text(self.driver,
                             self.logger,
                             MFPC.text_settins)
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         MFPC.text_settins)
        logger.info("Click 设置 end")

    def clickOnMyQueue(self):
        '''
        usage : Load "我的排队" page， according to textview in "我的排队", check "我的排队" page whether load correctly.
        '''
        logger.info("Click 我的排队 begin")
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
        logger.info("Click 点击我的排队 end")

    def clickOnMyTicket(self):
        '''
        usage : Load "我的票券" page， according to textview in "我的票券", check "我的票券" page whether load correctly.
        '''
        logger.info("Click 我的票券 begin")
        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_my_ticket)
        logger.info("Click 我的票券 end")

    def clickOnMyOrder(self):
        '''
        usage : Load "我的订单" page， according to textview in "我的订单", check "我的订单" page whether load correctly.
        '''
        logger.info("Click 我的订单 begin")
        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_my_order)
        logger.info("Click 我的订单 end")


    def clickOnMyLike(self):
        '''
        usage : Load "我的喜欢" page， according to textview in "我的喜欢", check "我的喜欢" page whether load correctly.
        '''
        logger.info("Click 我的喜欢 begin")
        API().clickElementByName(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  name = MFPC.text_my_like)
        logger.info("Click 我的喜欢 end")

    def isLoginStatus(self):
        try:
            API().find_view_by_resourceID_Until_android(self.driver,
                                                        self.logger,
                                                        MFPC.resource_id_txt_user_nick_name_tv)
            logger.info("Check login status, 已经注册")
            return True
        except TimeoutError:
            logger.info("Check login status, 没有注册")
            return False

    def clickOnParkingPayment(self):
        '''
        usage : Load "停车交费" page， according to textview in "停车交费", check "停车交费" page whether load correctly.
        '''
        # for _ in range(3):
        #     self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        self.scrollToParking()
        logger.info("Click 停车缴费 begin")
        API().clickElementByName(self.testcase, 
                                 self.driver, 
                                 self.logger,
                                 MFPC.text_parking_payment,
                                 MFPC.click_on_button_timeout)
        logger.info("Click 停车缴费 end")

    def scrollToParking(self):
        '''
        usage: 滑动到停车缴费
        '''
        API().iosScrollToElement(self.driver, self.logger,
                                 MFPC.xpath_parking_paymeng,
                                 MFPC.text_parking_payment)

    def validMyTicketsPage(self):
        '''
        usage: 验证我的票券页面是否加载出来
        '''
        logger.info("Check 我的票券 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_my_ticket,
                                 MFPC.click_on_button_timeout)
        logger.info("Check 我的票券 end")
        API().screenShot(self.driver, "myTicket")


    def gotoWodefeifantong(self):
        '''
        usage: 进入我的飞凡通
        '''

        API().iosScrollToElement(self.driver, self.logger,
                                 MFPC.xpath_myfeitongtong,
                                 MFPC.text_parking_payment)
        logger.info("Click 我的飞凡通 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_wodefeifantong,
                                 MFPC.click_on_button_timeout)
        logger.info("Click 我的飞凡通 end")

    def validLinghuaqian(self):
        '''
        usage: 验证零花钱
        '''
        logger.info("Check 零花钱 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  xpath = MFPC.xpath_linghuaqian)

        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=MFPC.text_linghuaqianyue)
        logger.info("Check 零花钱 end")
        API().screenShot(self.driver, "lingHuaQian")



    def validFukuaima(self):
        '''
        usage: 验证付款码
        '''
        logger.info("Check 付款码 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  xpath=MFPC.xpath_fukuanma)
        logger.info("Check 付款码 end")
        API().screenShot(self.driver, "fuKuanMa")

if __name__ == '__main__':
    pass;
