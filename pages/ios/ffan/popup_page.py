# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.popup_page_configs import PopupPageConfigs


class KeywordsType(object):
    '''
    This is a keywords type class.
    '''

    NAME = "name"
    XPATH = "xpath"


class ClickActivityKeywordsType(KeywordsType):
    '''
    This is a click activity keywords type class.
    '''


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

        self._validOperator = {VerifyActivityKeywordsType.NAME : self._validSelfByName,
                               VerifyActivityKeywordsType.XPATH : self._validSelfByXpath}

        self._clickOperator = {ClickActivityKeywordsType.NAME : self._clickOnButtonByName,
                               ClickActivityKeywordsType.XPATH : self._clickOnButtonByXpath}

    def _validSelfByName(self, keywords, assertable):
        '''
        usage: verify whether the current page is correct by resource id.
        '''

        if assertable:
            API().assertElementByName(self.testcase, self.driver, self.logger,
                                      keywords, PopupPageConfigs.assert_view_timeout)
        else:
            return API().validElementByName(self.driver, self.logger,
                                            keywords, PopupPageConfigs.verify_view_timeout)

    def _validSelfByXpath(self, keywords, assertable):
        '''
        usage: verify whether the current page is correct by text.
        '''

        if assertable:
            API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                       keywords, PopupPageConfigs.assert_view_timeout)
        else:
            return API().validElementByXpath(self.driver, self.logger,
                                             keywords, PopupPageConfigs.verify_view_timeout)

    def validSelf(self, keywords, keywordsType=VerifyActivityKeywordsType.NAME, assertable=True):
        '''
        usage: verify whether the current page is correct.
        '''

        return self._validOperator.get(keywordsType)(keywords, assertable)

    def _clickOnButtonByName(self, keywords):
        '''
        usage: click on the button by resource id.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 keywords, PopupPageConfigs.click_on_button_timeout)

    def _clickOnButtonByXpath(self, keywords):
        '''
        usage: click on the button by text.
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  keywords, PopupPageConfigs.click_on_button_timeout)

    def clickOnButton(self, keywords, keywordsType=ClickActivityKeywordsType.NAME):
        '''
        usage: click on a button.
        '''

        self._clickOperator.get(keywordsType)(keywords)

if __name__ == '__main__':
    pass
