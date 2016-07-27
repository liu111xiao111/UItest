# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.receive_success_page_configs import ReceiveSuccessPageConfigs as RSPC

class ReceiveSuccessPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>通用券=>领取成功
    '''
    def __init__(self, testcase, driver, logger):
        super(ReceiveSuccessPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证领取成功界面
        '''
        received_suc = API().validElementByText(self.driver,
                                                self.logger,
                                                RSPC.text_receive_success,
                                                45)
        if not received_suc:
            API().assertElementByContentDesc(self.testcase,
                                             self.driver,
                                             self.logger, 
                                             RSPC.content_desc_limit_dialog_text,
                                             45)
