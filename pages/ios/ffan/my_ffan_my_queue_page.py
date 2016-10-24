# -*- coding: utf-8 -*-

from pages.ios.ffan.my_ffan_my_queue_page_configs import MyFfanMyQueuePageConfigs
from api.api import API
from pages.ios.common.superPage import SuperPage

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
    def clickMoreRestaurant(self):
        '''
        usage:点击更多餐厅
        '''
        API().clickElementByName(testCase=self.testcase,driver=self.driver,logger=self.logger,
                                 name=MQPC.name_more_restauran)

    def validMoreRestaurant(self):
        '''
        usage:验证更多餐厅页面
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=MQPC.name_chafing)

if __name__ == '__main__':
    pass;