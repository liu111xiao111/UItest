# -*- coding:utf-8 -*-

import logging
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sharing_page_configs import SharingPageConfigs


class SharingPage(SuperPage):
    '''
    作者 宋波
    首页=>活动与优惠券=>活动详情=>分享
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SharingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SharingPageConfigs.resource_id_cancel_bt,
                                  SharingPageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  keywords, SharingPageConfigs.assert_view_timeout)

    def clickOnCancel(self):
        '''
        usage: click cancel button
        '''
        logging.info('Click on cancel button.')
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SharingPageConfigs.resource_id_cancel_bt,
                                 SharingPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
