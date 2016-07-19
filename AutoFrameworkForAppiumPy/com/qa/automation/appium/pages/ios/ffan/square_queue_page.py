# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.square_queue_page_configs import SquareQueuePageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

SQPC = SquareQueuePageConfigs()

class SquareQueuePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareQueuePage, self).__init__(testcase,
                                              driver,
                                              logger)

    def validSelf(self):
        '''
        usage : Click "排队取号" in square page, and load "排队取号" correctly.
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SQPC.resource_id_queue,
                                              seconds=18)

    def validQueueSuccess(self):
        '''
        usage: 检查是否取号成功
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  SQPC.verify_view_text,
                                                  SQPC.verify_view_timeout)

    def clicOnQueueNumber(self):
        '''
        usage: 点击 "取号"
        '''
        API().click_view_by_resourceID(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SQPC.text_queue_number)

    def inputNumberOfMeals(self):
        '''
        usage: 输入用餐人数
        '''
        '''API().input_view_by_xpath_ios(self.driver,
                                      self.logger,
                                      SQPC.xpath_number_of_meals,
                                      SQPC.number_of_meals)'''

    def clicOnGetQueueNumber(self):
        '''
        usage: Click "一键取号"
        '''
        API().input_view_by_xpath_ios(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SQPC.xpath_get_queue_number,
                                 SQPC.verify_click_timeout)

    def clickOnCancelQueue(self):
        '''
            Usage: Click on "取消排队"
        '''
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SQPC.xpath_cancel_queue,
                                  SQPC.verify_click_timeout)

if __name__ == '__main__':
    pass;