#!/usr/bin/env python
# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.seat_picking_page_configs import SeatPickingPageConfigs


class SeatPickingPage(SuperPage):
    '''
    This is seat picking page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SeatPickingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                                      SeatPickingPageConfigs.resource_id_seat_picking_title,
                                                      SeatPickingPageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger,
										keywords, SeatPickingPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
