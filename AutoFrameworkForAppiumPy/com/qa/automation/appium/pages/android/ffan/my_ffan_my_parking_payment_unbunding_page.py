# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_unbunding_page_configs import MyFfanMyParkingPaymentUnbundingPageConfigs


class MyFfanMyParkingPaymentUnbundingPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费=>输入车牌号码页=>更多=>解绑车牌确认提示页
    '''
    def __init__(self,testcase,driver,logger):
        super(MyFfanMyParkingPaymentUnbundingPage, self).__init__(testcase, driver, logger)

    def clickOnUnbundingBtn(self):
        '''
        usage: 点击"更多"
        ''' 
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         MyFfanMyParkingPaymentUnbundingPageConfigs.text_confirm,
                                         10)
