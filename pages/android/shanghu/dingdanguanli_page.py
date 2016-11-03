# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.dingdanguanli_page_configs import DingDanGuanLiPageConfigs as DDGLPC


class DingDanGuanLiPage(SuperPage):
    '''
    作者 乔佳溪
    订单管理
    '''
    def __init__(self, testcase, driver, logger):
        super(DingDanGuanLiPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到订单管理页
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DDGLPC.text_order_manager,
                                  DDGLPC.verify_timeout)

    def getOrderInfo(self):
        '''
        usage: 获取订单信息
        '''
        pass

    def clickOnOrderStatus(self):
        '''
        usage: 点击订单状态
        '''
        API().clickElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DDGLPC.content_desc_order_status,
                                        DDGLPC.verify_timeout)

    def clickOnClosedOrder(self):
        '''
        usage: 点击交易关闭
        '''
        API().clickElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DDGLPC.content_desc_closed_order,
                                        DDGLPC.verify_timeout)
