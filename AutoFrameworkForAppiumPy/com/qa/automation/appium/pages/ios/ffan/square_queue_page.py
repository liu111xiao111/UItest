# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.square_queue_page_configs import SquareQueuePageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

SQPC = SquareQueuePageConfigs()

class SquareQueuePage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>排队取号
    '''

    def __init__(self, testcase, driver, logger):
        super(SquareQueuePage, self).__init__(testcase,
                                              driver,
                                              logger)

    def validSelf(self):
        '''
        usage : Click "排队取号" in square page, and load "排队取号" correctly.
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=SQPC.resource_id_queue)

    def validQueueSuccess(self):
        '''
        usage: 检查是否取号成功
        '''
        successText = API().getTextByXpath(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  xpath=SQPC.xpath_view_text)

        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=successText,
                          expectText=SQPC.verify_view_text)

    def clicOnQueueNumber(self):
        '''
        usage: 点击 "取号"
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SQPC.text_queue_number)

    def inputNumberOfMeals(self):
        '''
        usage: 输入用餐人数
        '''
        API().inputStringByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SQPC.xpath_number_of_meals,
                                 SQPC.number_of_meals)

    def clicOnGetQueueNumber(self):
        '''
        usage: 点击 "一键取号"
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SQPC.xpath_get_queue_number,
                                  timeout = SQPC.verify_click_timeout)

    def clickOnCancelQueue(self):
        '''
            Usage: 点击 "取消排队"
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SQPC.xpath_cancel_queue,
                                  timeout = SQPC.verify_click_timeout)

if __name__ == '__main__':
    pass;