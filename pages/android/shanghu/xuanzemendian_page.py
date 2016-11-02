# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.xuanzemendian_page_configs import XuanZeMenDianPageConfigs as XZMDPC


class XuanZeMenDianPage(SuperPage):
    '''
    作者 乔佳溪
    选择门店
    '''
    def __init__(self, testcase, driver, logger):
        super(XuanZeMenDianPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到选择门店页,检查标题
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        XZMDPC.resource_id_title,
                                        XZMDPC.verify_timeout)

    def clickOnStore(self):
        '''
        usage: 选择门店
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           XZMDPC.text_store)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZMDPC.text_store,
                                 XZMDPC.verify_timeout)

    def clickOnConfirmBtn(self):
        '''
        usage: 点击确认按钮
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZMDPC.text_confirm,
                                 XZMDPC.verify_timeout)
