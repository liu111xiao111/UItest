# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.parking_payment_input_plate_number_page_configs import ParkingPaymentInputPlateNumberPageConfigs


class ParkingPaymentInputPlateNumberPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费=>输入车牌号码页
    '''

    def __init__(self,testcase,driver,logger):
        super(ParkingPaymentInputPlateNumberPage, self).__init__(testcase = testcase , driver = driver,logger = logger);


    def validSelf(self):
        '''
        usage : 判断"停车交费"标题显示是否正确 
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ParkingPaymentInputPlateNumberPageConfigs.name_parking_payment_title);

    def validLunbogundongtiao(self):
        '''
        usaage : 验证轮播滑动滚动条
        '''
        API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                   ParkingPaymentInputPlateNumberPageConfigs.xpath_lunbogundongtiao,
                                   ParkingPaymentInputPlateNumberPageConfigs.xpath_lunbogundongtiao)

    def inputPlateNumber(self):
        '''
        usage : 输入要绑定的车牌号
        '''
        API().inputStringByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 ParkingPaymentInputPlateNumberPageConfigs.xpath_plate_number,
                                 ParkingPaymentInputPlateNumberPageConfigs.plate_number)

        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = ParkingPaymentInputPlateNumberPageConfigs.name_return)

    def clickOnNextStep(self):
        '''
        usage: 点击下一步
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = ParkingPaymentInputPlateNumberPageConfigs.name_next_step)

if __name__ == '__main__':
    pass;