# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.feifan_card_bill_page_configs import FeiFanCardBillPageConfigs as FCBPC


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
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCBPC.resource_id_tv_bill_list_tv,
                                        30)

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
