# -*- coding: utf-8 -*-

from selenium.common.exceptions import TimeoutException

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_sign_on_page_configs import SignOnPageConfigs


class SignOnPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>签名
    '''

    def __init__(self, testcase, driver, logger):
        super(SignOnPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入广场模块，检查是否加载出来
    '''
    def validSelf(self):
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=SignOnPageConfigs.text_sign_on);

    def validChickedInStatus(self, assertable=True):
        '''
        usage: verify whether the status is checked.
        '''

        if assertable:
            API().find_view_by_content_desc_Until_android(self.driver, self.logger, SignOnPageConfigs.text_sign_in_button, SignOnPageConfigs.assert_view_timeout)
            return True
        else:
            try:
                API().find_view_by_content_desc_Until_android(self.driver, self.logger, SignOnPageConfigs.text_sign_in_button, SignOnPageConfigs.assert_view_timeout)
                return True
            except TimeoutException:
                return False

    def clickOnSignIn(self):
        '''
        usage: click on the sign in button.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, SignOnPageConfigs.xpath_sign_in_button, SignOnPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass;
