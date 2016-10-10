# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_page_configs import MyFfanMyParkingPaymentPageConfigs as PPPC


class MyFfanMyParkingPaymentPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费
    '''
    def __init__(self,testcase,driver,logger):
        super(MyFfanMyParkingPaymentPage, self).__init__(testcase, driver, logger);


    def validSelf(self):
        '''
        usage : 判断“付停车费”是否正确显示
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        PPPC.resource_id_tv_parking_payment_tv,
                                        10)

    def inputVIN(self):
        '''
        usage : 输入车牌号
        ''' 
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      PPPC.resource_id_tv_VIN_tv,
                                      PPPC.input_VIN,
                                      10)

    def clickOnNextBtn(self):
        '''
        usage: 点击"下一步"
        ''' 
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PPPC.text_next_btn,
                                 10)

    def clickAndValidItems(self, item = "default", title = "default"):
        '''
        usage: 点击各入口项目
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 item,
                                 60)
        API().waitBySeconds(2)
        API().assertElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 title,
                                 60)
        API().clickBackKeyForAndroid(self.driver, self.logger)
