# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.lefu_pay_way_page_configs import LefuPayWayPageConfigs as LPWPC
from pages.logger import logger


class LefuPayWayPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付=>输入乐付消费金额页=>选择支付方式页
    '''
    def __init__(self, testcase, driver, logger):
        super(LefuPayWayPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证支付方式页
        '''
        logger.info("Check 支付方式页面 begin")
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        LPWPC.resource_id_pay_way,
                                        18)
        logger.info("Check 支付方式页面 end")

    def getOrderNumber(self):
        '''
        usage : 获取数值
        '''
        orderNumber = API().getTextByResourceId(self.testcase, self.driver, self.logger,
                                                LPWPC.resource_id_order_number,
                                                10)
        return orderNumber

    def clickOnConfirm(self):
        '''
        usage : 点击 "确认"
        '''
        logger.info("Click 确认 begin")
#         API().clickBackKeyForAndroid(self.driver, self.logger)
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                       LPWPC.xpath_back,
                                       10)
        API().waitBySeconds(2)
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                       LPWPC.text_confirm,
                                       10)
        logger.info("Click 确认 end")

