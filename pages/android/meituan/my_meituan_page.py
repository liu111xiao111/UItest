# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.meituan.my_meituan_page_configs import MyMeituanPageConfigs as MMPC
from pages.logger import logger


class MyMeituanPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>我的页面
    '''
    def __init__(self, testcase, driver, logger):
        super(MyMeituanPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到我的页面
        '''
        logger.info("Check 我的页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMPC.text_my_order,
                                  MMPC.verify_view_timeout)
        logger.info("Check 我的页面 end")

    def validLoginStatus(self):
        '''
        usage : 进入到我的页面
        '''
        logger.info("Check 是否登录状态 begin")
        loginStatus = API().validElementByText(self.driver,
                                               self.logger,
                                               MMPC.text_click_login,
                                               MMPC.verify_view_timeout)
        logger.info("Check 是否登录状态 end")
        return loginStatus

    def clickOnLogin(self):
        '''
        usage: 点击登录按钮
        '''
        logger.info("Click 登录 begin")
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MMPC.text_click_login,
                                       MMPC.click_view_timeout)
        logger.info("Check 登录 end")

    def clickOnSetting(self):
        '''
        usage: 点击设置
        '''
        logger.info("Click 设置 icon begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MMPC.resource_id_setting,
                                       MMPC.click_view_timeout)
        logger.info("Check 设置 icon end")

    def clickOnLogout(self):
        '''
        usage: 点击退出登录
        '''
        logger.info("Click 退出登录 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMPC.text_logout,
                                 MMPC.click_view_timeout)

        API().screenShot(self.driver, "tuiChuZhangHu")

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMPC.xpath_exit,
                                  MMPC.click_view_timeout)
#         API().clickElementByText(self.testcase,
#                                  self.driver,
#                                  self.logger,
#                                  MMPC.text_exit,
#                                  MMPC.click_view_timeout)

        logger.info("Check 退出登录 end")

    def clickOnMyOrder(self):
        '''
        usage: 点击我的订单
        '''
        logger.info("Click 我的订单 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMPC.text_my_order,
                                 MMPC.click_view_timeout)
        logger.info("Check 我的订单 end")


    def clickOnToBePaid(self):
        '''
        usage : 点击我的订单待付款
        '''
        logger.info("Click 待付款 begin")
        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMPC.xpath_to_be_paid,
                                 MMPC.click_view_timeout)
        logger.info("Click 待付款 end")

    def validSelfToBePaid(self):
        '''
        usage : 进入待付款页面，判断显示是否正确
        '''
        logger.info("Check 待付款页面 start")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMPC.text_to_be_paid,
                                  MMPC.verify_view_timeout)
        logger.info("Check 待付款页面 end")

    def clickOnUse(self):
        '''
        usage : 点击我的订单可使用
        '''
        logger.info("Click 可使用 begin")
        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMPC.xpath_use,
                                 MMPC.click_view_timeout)
        logger.info("Click 可使用 end")

    def validSelfUse(self):
        '''
        usage : 进入可使用页面，判断显示是否正确
        '''
        logger.info("Check 可使用页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMPC.text_use,
                                  MMPC.verify_view_timeout)
        logger.info("Check 可使用页面 end")

    def clickOnComments(self):
        '''
        usage : 点击我的订单我的点评
        '''
        logger.info("Click 我的点评 begin")
        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMPC.xpath_comments,
                                 MMPC.click_view_timeout)
        logger.info("Click 我的点评 end")

    def validSelfCommets(self):
        '''
        usage : 进入我的点评页面，判断显示是否正确
        '''
        logger.info("Check 我的点评页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMPC.text_comments,
                                  MMPC.verify_view_timeout)
        logger.info("Check 我的点评页面 end")

    def clickOnReturnRefund(self):
        '''
        usage : 点击我的订单退货退款
        '''
        logger.info("Click 退货退款 begin")
        API().clickElementByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MMPC.xpath_return_refund,
                                 MMPC.click_view_timeout)
        logger.info("Click 退货退款 end")

    def validSelfReturnRefund(self):
        '''
        usage : 进入退货退款页面，判断显示是否正确
        '''
        logger.info("Check 退货退款页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MMPC.text_return_refund,
                                  MMPC.verify_view_timeout)
        logger.info("Check 退货退款页面 end")
