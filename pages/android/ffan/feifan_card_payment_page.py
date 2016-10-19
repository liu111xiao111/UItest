# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.feifan_card_payment_page_configs \
import FeiFanCardPaymentPageConfigs as FCPPC


class FeiFanCardPaymentPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>飞凡卡=>飞凡卡付款
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPaymentPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 检查是否加载出来
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPPC.resource_id_tv_payment_list_tv,
                                        FCPPC.verify_button_timeout)
