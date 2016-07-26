# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_more_page_configs import MyFfanMyParkingPaymentMorePageConfigs as PPMPC


class MyFfanMyParkingPaymentMorePage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费=>输入车牌号码页=>更多
    '''
    def __init__(self,testcase,driver,logger):
        super(MyFfanMyParkingPaymentMorePage, self).__init__(testcase, driver, logger)


    def validSelf(self):
        '''
        usage : 验证停车缴费
        ''' 
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        PPMPC.text_unbunding,
                                        10)

    def clickOnUnbundingBtn(self):
        '''
            usage: 点击"更多"
        ''' 
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PPMPC.text_unbunding,
                                 10)
