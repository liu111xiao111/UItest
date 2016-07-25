# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.movie_details_page_configs import MovieDetailsPageConfigs as MDPC


class MovieDetailsPage(SuperPage):
    '''
    作者 陈诚
    首页=>电影=>电影细节页面
    '''
    def __init__(self, testcase, driver, logger):
        super(MovieDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证电影细节页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MDPC.resource_id_movie_details_title,
                                        MDPC.assert_view_timeout)

    def clickOnTomorrowsDate(self):
        '''
        usage: 点击明日信息
        '''

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MDPC.xpath_tomorrows_date_button,
                                  MDPC.click_on_button_timeout)

    def clickOnSubCinema(self):
        '''
        usage: 点击附属电影
        '''

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MDPC.resource_id_sub_cinema_button,
                                       MDPC.click_on_button_timeout)
