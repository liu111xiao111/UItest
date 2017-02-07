# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_ffan_my_queue_page_configs import MyFfanMyQueuePageConfigs as MQPC
from pages.logger import logger


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
        logger.info("Check 我的排队 begin")
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MQPC.text_queue_title,
                                        30)
        logger.info("Check 我的排队 end")

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

    def clickOnMoreRestaurant(self):
        '''
        usage : 点击更多餐厅
        '''
        logger.info("Click 更多餐厅 begin")
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MQPC.text_more_restaurant,
                                       30)
        logger.info("Click 更多餐厅 end")
