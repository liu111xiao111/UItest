# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.meituan.dashboard_page_configs import DashboardPageConfigs as DPC
from pages.logger import logger


class DashboardPage(SuperPage):
    '''
    作者： 乔佳溪
    首页
    '''
    def __init__(self, testcase, driver, logger):
        super(DashboardPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到应用首页
        '''
        logger.info("Check 首页 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.text_dashboard,
                                  DPC.assert_timeout)
        logger.info("Check 首页 end")

    def clickOnMy(self):
        '''
        usage： 点击我的
        '''
        logger.info("Click 我的 begin")
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.text_mine,
                                  DPC.assert_timeout)
        logger.info("Click 我的 end")

    def clickOnFood(self):
        '''
        usage： 点击美食
        '''
        logger.info("Click 美食 begin")
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.text_food,
                                  DPC.assert_timeout)
        logger.info("Click 美食 end")

    def clickOnDashboard(self):
        '''
        usage： 点击首页
        '''
        logger.info("Click 首页 begin")
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.text_dashboard,
                                  DPC.assert_timeout)
        logger.info("Click 首页 end")

    def scrollOnPage(self):
        '''
        usage: 页面内滑动
        '''
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for i in range(20):
            if i % 2 == 0:
                API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
            else:
                API().scroll(self.driver, self.logger, width / 2, hight / 3, width / 2, hight / 2)

    def clickOnMovie(self):
        '''
        usage: 点击"电影"类目
        '''
        logger.info("Click 电影 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_movie_button,
                                 DPC.assert_timeout)
        logger.info("Click 电影 end")
