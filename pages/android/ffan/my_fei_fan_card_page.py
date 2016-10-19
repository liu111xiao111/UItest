# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_fei_fan_card_page_configs import MyFeiFanCardPageConfigs as MFCPC


class MyFeiFanCardPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡
    '''
    def __init__(self, testcase, driver, logger):
        super(MyFeiFanCardPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证我的飞凡卡
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MFCPC.resource_id_my_fei_fan_card_title,
                                        MFCPC.assert_view_timeout)

    def clickOnTransactionRecord(self):
        '''
        usage: 点击交易记录
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFCPC.text_transaction_record_button,
                                 MFCPC.click_on_button_timeout)

    def clickOnPayemntsSettings(self):
        '''
        usage: 点击付款设置
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFCPC.text_payments_settings_button,
                                 MFCPC.click_on_button_timeout)
