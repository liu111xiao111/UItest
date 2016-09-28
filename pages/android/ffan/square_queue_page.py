# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_queue_page_configs import SquareQueuePageConfigs as SQPC


class SquareQueuePage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>排队取号
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareQueuePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 点击 "排队取号"
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SQPC.resource_id_queue,
                                        18)

    def validQueueSuccess(self):
        '''
        usage: 检查是否取号成功
        '''
        text_list = [SQPC.verify_view_text_1, SQPC.verify_view_text_2]
        API().assertElementsByContentDescs(self.testcase,
                                           self.driver,
                                           self.logger,
                                           text_list,
                                           SQPC.verify_view_timeout)

    def clicOnQueueNumber(self):
        '''
        usage: 点击 "取号"
        '''
        if API().validElementByText(self.driver, self.logger, SQPC.text_queue_number):
            API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     SQPC.text_queue_number,
                                     SQPC.verify_click_timeout)
            return True
        else:
            return False

    def inputNumberOfMeals(self):
        '''
        usage: 输入人数
        '''
        API().inputStringByClassName(self.testcase,
                                     self.driver,
                                     self.logger,
                                     SQPC.class_name_number_of_meals,
                                     SQPC.number_of_meals,
                                     SQPC.verify_input_timeout)

    def clicOnGetQueueNumber(self):
        '''
        usage: 点击 "一键取号"
        '''
        API().clickElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SQPC.text_get_queue_number,
                                        SQPC.verify_click_timeout)

    def clickOnCancelQueue(self):
        '''
        Usage: 点击 "取消排队"
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SQPC.xpath_cancel_queue,
                                  SQPC.verify_click_timeout)

    def validGetQueue(self):
        '''
        usage : 判断是否能够 "取号"
        '''
        API().validElementByText(self.driver,
                                 self.logger,
                                 SQPC.text_queue_number,
                                 SQPC.verify_view_timeout)
