# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.popup_page_configs import PopupPageConfigs as PPC


class KeywordsType(object):
    '''
    作者 刘涛
    usage: 关键值类型类
    '''

    RESOURCE_ID = "resource_id"
    TEXT = "text"
    XPATH = "xpath"


class ClickActivityKeywordsType(KeywordsType):
    '''
    作者 刘涛
    usage: 点击页面关键值类型类
    '''

    CONTENT_DESC = "content-desc"


class VerifyActivityKeywordsType(KeywordsType):
    '''
    作者 刘涛
    usage: 验证页面关键值类型类
    '''


class PopupPage(SuperPage):
    '''
    作者 刘涛
    usage: 弹出框
    '''
    def __init__(self, testcase, driver, logger):
        super(PopupPage, self).__init__(testcase, driver, logger)

        self._validOperator = {VerifyActivityKeywordsType.RESOURCE_ID : self._validSelfByResourceId,
                               VerifyActivityKeywordsType.TEXT : self._validSelfByText,
                               VerifyActivityKeywordsType.XPATH: self._validSelfByXpath}

        self._clickOperator = {ClickActivityKeywordsType.RESOURCE_ID : self._clickOnButtonByResourceId,
                               ClickActivityKeywordsType.TEXT : self._clickOnButtonByText,
                               ClickActivityKeywordsType.XPATH: self._clickOnButtonByXpath}

    def _validSelfByResourceId(self, keywords, assertable):
        '''
        usage: 通过resource id 验证页面
        '''
        if assertable:
            API().assertElementByResourceId(self.testcase,
                                            self.driver,
                                            self.logger,
                                            keywords,
                                            PPC.assert_view_timeout)
            return True
        else:
            return API().validElementByResourceId(self.driver,
                                                  self.logger,
                                                  keywords,
                                                  PPC.verify_view_timeout)

    def _validSelfByText(self, keywords, assertable):
        '''
        usage: 通过text验证页面
        '''

        if assertable:
            API().assertElementByText(self.testcase,
                                      self.driver,
                                      self.logger,
                                      keywords,
                                      PPC.assert_view_timeout)
            return True
        else:
            return API().validElementByText(self.driver,
                                            self.logger,
                                            keywords,
                                            PPC.verify_view_timeout)

    def _validSelfByXpath(self, keywords, assertable):
        '''
        usage: 通过xpath验证页面
        '''

        if assertable:
            API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                      keywords, PPC.assert_view_timeout)
        else:
            return API().validElementByXpath(self.driver, self.logger,
                                            keywords, PPC.verify_view_timeout)

    def validSelf(self, keywords, keywordsType=VerifyActivityKeywordsType.RESOURCE_ID, assertable=True):
        '''
        usage: 验证当前页面
        '''

        return self._validOperator.get(keywordsType)(keywords, assertable)

    def _clickOnButtonByResourceId(self, keywords):
        '''
        usage: 通过resource id点击按钮
        '''

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       keywords,
                                       PPC.click_on_button_timeout)

    def _clickOnButtonByText(self, keywords):
        '''
        usage: 通过text点击按钮
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 keywords,
                                 PPC.click_on_button_timeout)

    def _clickOnButtonByXpath(self, keywords):
        '''
        usage: 通过xpath点击按钮
        '''

        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 keywords, PPC.click_on_button_timeout)

    def clickOnButton(self, keywords, keywordsType=ClickActivityKeywordsType.RESOURCE_ID):
        '''
        usage: 点击按钮
        '''
        self._clickOperator.get(keywordsType)(keywords)
