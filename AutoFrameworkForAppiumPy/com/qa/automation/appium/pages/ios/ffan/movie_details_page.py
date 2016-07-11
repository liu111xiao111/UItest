# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.movie_details_page_configs import MovieDetailsPageConfigs


class MovieDetailsPage(SuperPage):
    '''
    This is a movie details page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MovieDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the switch city page.
        '''

        API().assert_view_by_xpath_android(self.testcase, self.driver, self.logger, MovieDetailsPageConfigs.xpath_movie_details_title_st, MovieDetailsPageConfigs.assert_view_timeout)

    def clickOnTomorrowsDate(self):
        '''
        usage: click tomorrow's date button
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, MovieDetailsPageConfigs.xpath_tomorrows_date_button, MovieDetailsPageConfigs.click_on_button_timeout)

    def clickOnSubCinema(self):
        '''
        usage: click on a sub-cinema button
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, MovieDetailsPageConfigs.xpath_sub_cinema_st, MovieDetailsPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
