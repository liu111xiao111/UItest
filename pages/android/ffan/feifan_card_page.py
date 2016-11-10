# -*- coding: utf-8 -*-

from pages.android.ffan.feifan_card_page_configs import FeiFanCardPageConfigs
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.logger import logger

FCPC = FeiFanCardPageConfigs()

class FeiFanCardPage(SuperPage):
    '''
    作者：刘涛
    首页=>飞凡卡
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 检查飞凡卡界面
        '''
        logger.info("Check 飞凡通 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_bill_tv,
                                        FCPC.verify_view_timeout)
        logger.info("Check 飞凡通 end")

    def clickOnOpenCard(self):
        '''
        usage: 点击市民/公交卡
        '''
        API().clickElementByText(self.testcase,
                                self.driver,
                                self.logger,
                                FCPC.text_tv_open_tv,
                                FCPC.verify_click_timeout)

    def clickOnPayment(self):
        '''
        usage : 点击付款
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_payment_tv,
                                       FCPC.verify_click_timeout)

    def clickOnCardManager(self):
        '''
        usage : 点击卡管家
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_card_manager_tv,
                                       FCPC.verify_click_timeout)

    def clickOnCharge(self):
        '''
        usage : 点击零花钱
        '''
        logger.info("Click 零花钱 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_charge_tv,
                                       FCPC.verify_click_timeout)
        logger.info("Click 零花钱 end")

    def clickOnBill(self):
        '''
        usage : 点击账单
        '''
        logger.info("Click 账单 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_bill_tv,
                                       FCPC.verify_click_timeout)
        logger.info("Click 账单 end")

    def clickOnCodeIcon(self):
        '''
        usage : 点击扫码图标
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_code_icon_tv,
                                       FCPC.verify_click_timeout)

    def clickOnPaymentCode(self):
        '''
        usage : 点击付款码
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 FCPC.text_tv_payment_code_tv,
                                 FCPC.verify_click_timeout)

    def clickOnPocketMoney(self):
        '''
        usage : 点击零花钱
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_pocket_money_tv,
                                       FCPC.verify_click_timeout)

    def clickOnIntegral(self):
        '''
        usage : 点击积分
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 FCPC.text_integral,
                                 FCPC.verify_click_timeout)
