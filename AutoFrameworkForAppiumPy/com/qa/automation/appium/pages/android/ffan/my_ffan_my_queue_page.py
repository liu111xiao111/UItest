# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.my_ffan_my_queue_page_configs import MyFfanMyQueuePageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

MQPC = MyFfanMyQueuePageConfigs()

class MyFfanMyQueuePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyQueuePage, self).__init__(testcase,
                                                driver,
                                                logger)

    def validSelf(self):
        '''
        usage : Click "我的排队" in my Feifan page， and load "我的排队" page correctly. 
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              MQPC.resource_id_tv_registration_tv)


if __name__ == '__main__':
    pass;