#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium.common.exceptions import TimeoutException

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.popup_page_configs import PopupPageConfigs


class KeywordsType(object):
    '''
    This is a keywords type class.
    '''


    RESOURCE_ID = "resource_id"
    TEXT = "text"

class ClickActivityKeywordsType(KeywordsType):
    '''
    This is a click activity keywords type class.
    '''


    XPATH = "xpath"
    CONTENT_DESC = "content-desc"

class VerifyActivityKeywordsType(KeywordsType):
    '''
    This is a verify activity keywords type class.
    '''

class PopupPage(SuperPage):
    '''
    This is a Popup page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(PopupPage, self).__init__(testcase, driver, logger)

        self._validOperator = {VerifyActivityKeywordsType.RESOURCE_ID : self._validSelfByResourceId,
                               VerifyActivityKeywordsType.TEXT : self._validSelfByText}

        self._clickOperator = {ClickActivityKeywordsType.RESOURCE_ID : self._clickOnButtonByResourceId,
                               ClickActivityKeywordsType.TEXT : self._clickOnButtonByText}

    def _validSelfByResourceId(self, keywords, assertable):
        '''
        usage: verify whether the current page is correct by resource id.
        '''

        if assertable:
            API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, keywords, PopupPageConfigs.assert_view_timeout)
            return True
        else:
            try:
                API().find_view_by_resourceID_Until_android(self.driver, self.logger, keywords, PopupPageConfigs.verify_view_timeout)
                return True
            except TimeoutException:
                return False

    def _validSelfByText(self, keywords, assertable):
        '''
        usage: verify whether the current page is correct by text.
        '''

        if assertable:
            API().assert_view_by_text_android(self.testcase, self.driver, self.logger, keywords, PopupPageConfigs.assert_view_timeout)
            return True
        else:
            try:
                API().find_view_by_text_Until_android(self.driver, self.logger, keywords, PopupPageConfigs.verify_view_timeout)
                return True
            except TimeoutException:
                return False

    def validSelf(self, keywords, keywordsType=VerifyActivityKeywordsType.RESOURCE_ID, assertable=True):
        '''
        usage: verify whether the current page is correct.
        '''

        return self._validOperator.get(keywordsType)(keywords, assertable)

    def _clickOnButtonByResourceId(self, keywords):
        '''
        usage: click on the button by resource id.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, keywords, PopupPageConfigs.click_on_button_timeout)

    def _clickOnButtonByText(self, keywords):
        '''
        usage: click on the button by text.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, keywords, PopupPageConfigs.click_on_button_timeout)

    def clickOnButton(self, keywords, keywordsType=ClickActivityKeywordsType.RESOURCE_ID):
        '''
        usage: click on a button.
        '''

        self._clickOperator.get(keywordsType)(keywords)

if __name__ == '__main__':
    pass
