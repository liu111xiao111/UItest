# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.meituan.movie_page_configs import MoviePageConfigs as MPC
from pages.logger import logger


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
        logger.info("Check 电影页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MPC.text_movie_title,
                                  MPC.assert_view_timeout)
        logger.info("Check 电影页面 end")

    def clickOnCheckAll(self):
        '''
        usage: 点击查看全部
        '''
        logger.info("Click 查看全部 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MPC.text_check_all,
                                 MPC.click_on_button_timeout)
        logger.info("Click 查看全部 end")

    def clickOnSeatPickingAndBuyingTicket(self):
        '''
        usage: 点击座位信息
        '''
        logger.info("Click 选座购票 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MPC.resource_id_seat_picking_and_buying_ticket_button,
                                       MPC.click_on_button_timeout)
        logger.info("Click 选座购票 end")

