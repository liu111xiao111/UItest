# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.movie_page_configs import MoviePageConfigs as MPC


class MoviePage(SuperPage):
    '''
    作者 陈诚
    首页=>电影页面
    '''
    def __init__(self, testcase, driver, logger):
        super(MoviePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证电影页面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MPC.text_movie_title,
                                  MPC.assert_view_timeout)

    def clickOnSeatPickingAndBuyingTicket(self):
        '''
        usage: 点击座位信息
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MPC.resource_id_seat_picking_and_buying_ticket_button,
                                       MPC.click_on_button_timeout)
