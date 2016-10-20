# -*- coding: utf-8 -*-


from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.square_sign_on_page_configs import SignOnPageConfigs


class SignOnPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>签名
    '''

    def __init__(self, testcase, driver, logger):
        super(SignOnPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 进入广场模块，检查是否加载出来
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SignOnPageConfigs.name_daily_see_st,
                                  SignOnPageConfigs.assert_view_timeout)

    def validChickedInStatus(self, assertable=True):
        '''
        usage: verify whether the status is checked.
        '''

        tempTest = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                        SignOnPageConfigs.xpath_sign_in_st,
                                        SignOnPageConfigs.assert_view_timeout)

        if assertable:
#             API().assertElementByName(self.testcase, self.driver, self.logger,
#                                       SignOnPageConfigs.name_chicked_in_st,
#                                       SignOnPageConfigs.assert_view_timeout)
            API().assertTrue(self.testcase, self.logger,
                             tempTest == SignOnPageConfigs.name_chicked_in_st)
        else:
#             return API().validElementByName(self.driver, self.logger,
#                                             SignOnPageConfigs.name_chicked_in_st,
#                                             SignOnPageConfigs.assert_view_timeout)
            return tempTest == SignOnPageConfigs.name_chicked_in_st

    def clickOnSignIn(self):
        '''
        usage: click on the sign in button.
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                 SignOnPageConfigs.xpath_sign_in_st,
                                 SignOnPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass;
