#!/usr/bin/env python
# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.cinema_page_configs import CinemaPageConfigs


class CinemaPage(SuperPage):
    '''
    This is hui life page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(CinemaPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until_android(self.testcase, self.driver, self.logger,
                                                      CinemaPageConfigs.resource_id_cinema_title,
                                                      CinemaPageConfigs.assert_view_timeout)

    def clickOnBuyTicket(self):
        '''
        usage: click on the buy ticket button.
        '''

        API().click_view_by_resourceID_android(self.testcase, self.driver, self.logger,
                                               CinemaPageConfigs.resource_id_buy_ticket_button,
                                               CinemaPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
