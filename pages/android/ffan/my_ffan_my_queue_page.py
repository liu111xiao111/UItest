# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_ffan_my_queue_page_configs import MyFfanMyQueuePageConfigs as MQPC


class MyFfanMyQueuePage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的排队
    '''
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyQueuePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证我的排队
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MQPC.resource_id_tv_registration_tv,
                                        10)

    def clickOnCancelQueue(self):
        '''
        usage : 取消排队
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MQPC.resource_id_tv_cancel_queue_tv,
                                       10)
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MQPC.resource_id_tv_certain_tv,
                                       10)
