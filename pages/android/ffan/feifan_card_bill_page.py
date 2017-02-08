# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.feifan_card_bill_page_configs import FeiFanCardBillPageConfigs as FCBPC
from pages.logger import logger


class FeiFanCardBillPage(SuperPage):
    '''
    作者 宋波
    首页=>飞凡卡=>飞凡卡账单
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardBillPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 检查是否加载出来
        '''
        logger.info("Check 零花钱页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCBPC.resource_id_tv_bill_list_tv,
                                        30)
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCBPC.text_linghuaqian_title,
                                        30)
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCBPC.text_chongzhi_button,
                                        30)
        logger.info("Check 零花钱页面 end")

    def validSelfBill(self):
        '''
        usage : 检查是否加载出来
        '''
        logger.info("Check 飞凡通账单页面 begin")
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCBPC.text_zhangdan_title,
                                        30)
        logger.info("Check 飞凡通账单页面 end")

    def validSubFilterByText(self, text=u"全部"):
        '''
        usage: 验证子标签
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  text,
                                  FCBPC.click_on_button_timeout)

    def clickOnFilter(self):
        '''
        usage: 点击标签
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCBPC.resource_id_filter_button,
                                       FCBPC.click_on_button_timeout)

    def clickOnSubFilterByText(self, text=u"全部"):
        '''
        usage: 点击子标签
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 text,
                                 FCBPC.click_on_button_timeout)
