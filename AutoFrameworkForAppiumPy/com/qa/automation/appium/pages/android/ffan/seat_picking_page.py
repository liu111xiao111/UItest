# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.seat_picking_page_configs import SeatPickingPageConfigs as SPPC


class SeatPickingPage(SuperPage):
    '''
    作者 陈诚
    首页=>电影=>座位信息界面
    '''

    def __init__(self, testcase, driver, logger):
        super(SeatPickingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证座位采集界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPPC.resource_id_seat_picking_title,
                                        SPPC.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  keywords,
                                  SPPC.assert_view_timeout)
