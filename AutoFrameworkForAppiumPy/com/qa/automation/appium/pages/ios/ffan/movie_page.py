#!/usr/bin/env python
# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.movie_page_configs import MoviePageConfigs


class MoviePage(SuperPage):
    '''
    作者 宋波
    首页=>电影
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MoviePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the switch city page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, MoviePageConfigs.text_movie_title, MoviePageConfigs.assert_view_timeout)

    def clickOnSeatPickingAndBuyingTicket(self):
        '''
        usage: click seat picking and buying ticket button
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, MoviePageConfigs.xpath_seat_picking_and_buying_ticket_bt, MoviePageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
