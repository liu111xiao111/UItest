# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_queue_page_configs import MyFfanMyQueuePageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

MQPC = MyFfanMyQueuePageConfigs()

class MyFfanMyQueuePage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的排队
    '''

    def __init__(self, testcase, driver, logger):
        super(MyFfanMyQueuePage, self).__init__(testcase,
                                                driver,
                                                logger)

    def validSelf(self):
        '''
        usage : Click "我的排队" in my Feifan page， and load "我的排队" page correctly. 
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=MQPC.resource_id_tv_registration_tv)

if __name__ == '__main__':
    pass;