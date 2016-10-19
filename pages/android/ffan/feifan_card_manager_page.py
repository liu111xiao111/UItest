# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.feifan_card_manager_page_configs \
import FeiFanCardManagerPageConfigs as FCMPC


class FeiFanCardManagerPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>飞凡卡=>卡管家
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardManagerPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 检查是否加载出来
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCMPC.resource_id_tv_manager_list_tv,
                                        FCMPC.verify_button_timeout)
