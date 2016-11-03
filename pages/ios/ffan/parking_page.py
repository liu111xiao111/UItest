# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.ffan.parking_page_configs import ParkingPageConfigs
from pages.ios.common.superPage import SuperPage


class ParkingPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车
    '''

    def __init__(self, testcase, driver, logger):
        super(ParkingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")

    def clickOnParkingPayment(self):
        '''
        usage: 点击"停车交费".
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = ParkingPageConfigs.name_parking_payment)
        
    def clickOnZhaoche(self):
        '''
        usage: 点击"找车".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchezhaoche,
                                  ParkingPageConfigs.click_on_button_timeout)
    
    def validZhaoche(self):
        notFindGpsSquare = API().validElementByName(self.driver, self.logger, ParkingPageConfigs.name_not_gps_square)
        if notFindGpsSquare == False:
            API().assertElementByIosUiautomation(self.testcase,self.driver,self.logger
                 ,uiaString=".navigationBars()[0]")
            self.clickBackKey()
        else:
            API().clickElementByName(self.testcase, self.driver, self.logger, ParkingPageConfigs.name_know_text)
        
    def clickOnFujintingche(self):
        '''
        usage: 点击"附近停车场".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_fujintingchechang,
                                  ParkingPageConfigs.click_on_button_timeout)
    
    def validFujintingche(self):
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
    
    def clickOnTingchequan(self):
        '''
        usage: 点击"停车券".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchequan,
                                  ParkingPageConfigs.click_on_button_timeout)
    def validTingchequan(self):
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
        
    def clickOnTingchejilu(self):
        '''
        usage: 点击"停车记录".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchejilu,
                                  ParkingPageConfigs.click_on_button_timeout)
    def validTingchejilu(self):
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
    
    def clickOnHelp(self):
        '''
        usage: 点击"帮助".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_bangzhu,
                                  ParkingPageConfigs.click_on_button_timeout)
    def validHelp(self):
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")

if __name__ == '__main__':
    pass;
