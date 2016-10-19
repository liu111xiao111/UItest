# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.receive_success_page_configs import ReceiveSuccessPageConfigs


class ReceiveSuccessPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>通用券=>领取成功
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(ReceiveSuccessPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''
        received_suc = API().validElementByName(self.driver, self.logger,
                                                ReceiveSuccessPageConfigs.text_receive_success,
                                                10)
        if not received_suc:
            API().assertElementByName(self.testcase, self.driver, self.logger,
                                      ReceiveSuccessPageConfigs.content_desc_limit_dialog_text,
                                      10)


    def getPrivilegeCouponCode(self):
        '''
        usage: get the privilege coupon code.
        '''
        return API().getTextByXpath(self.testcase, self.driver, self.logger, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[6]', 10)


if __name__ == '__main__':
    pass
