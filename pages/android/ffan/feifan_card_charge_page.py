# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.feifan_card_charge_page_configs import FeiFanCardChargePageConfigs as FCCPC
from pages.logger import logger


class FeiFanCardChargePage(SuperPage):
    '''
    作者 乔佳溪
    首页=>飞凡卡=>我的零花钱
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardChargePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 检查是否加载出来
        '''
        logger.info("Check 零花钱 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCCPC.text_tv_charge_tv,
                                  FCCPC.verify_button_timeout)
        logger.info("Check 零花钱 end")

    def clickOnBill(self):
        '''
        usage: 点击账单
        '''
        logger.info("Click 账单 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 FCCPC.text_tv_bill_tv,
                                 FCCPC.click_on_button_timeout)
        logger.info("Click 账单 end")
