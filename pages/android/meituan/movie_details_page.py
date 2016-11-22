# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.meituan.movie_details_page_configs import MovieDetailsPageConfigs as MDPC
from pages.logger import logger


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
        logger.info("Check 电影详细页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MDPC.text_details_film,
                                  MDPC.assert_view_timeout)
        logger.info("Check 电影详细页面 end")

    def validCheckall(self):
        '''
        usage: 验证查看全部电影页面
        '''
        logger.info("Check 查看全部电影页面 begin")
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MDPC.text_all_film,
                                        MDPC.assert_view_timeout)
        logger.info("Check 查看全部电影页面 end")

    def clickOnBuyingTicket(self):
        '''
        usage: 点击购票
        '''
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  MDPC.text_buy_ticket,
                                  MDPC.click_on_button_timeout)
