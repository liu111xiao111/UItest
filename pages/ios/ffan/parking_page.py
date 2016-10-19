# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.ffan.parking_page_configs import ParkingPageConfigs
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class ParkingPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车
    '''

    def __init__(self, testcase, driver, logger):
        super(ParkingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=ParkingPageConfigs.name_parking_navigation_bar)

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
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=ParkingPageConfigs.name_zhaoche)
        
    def clickOnFujintingche(self):
        '''
        usage: 点击"附近停车场".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_fujintingchechang,
                                  ParkingPageConfigs.click_on_button_timeout)
    
    def validFujintingche(self):
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=ParkingPageConfigs.name_fujintingche)
    
    def clickOnTingchequan(self):
        '''
        usage: 点击"停车券".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchequan,
                                  ParkingPageConfigs.click_on_button_timeout)
    def validTingchequan(self):
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=ParkingPageConfigs.name_tingchequan)
        
    def clickOnTingchejilu(self):
        '''
        usage: 点击"停车记录".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchejilu,
                                  ParkingPageConfigs.click_on_button_timeout)
    def validTingchejilu(self):
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=ParkingPageConfigs.name_tingchejilu)
    
    def clickOnHelp(self):
        '''
        usage: 点击"帮助".
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_bangzhu,
                                  ParkingPageConfigs.click_on_button_timeout)
    def validHelp(self):
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=ParkingPageConfigs.name_help)

if __name__ == '__main__':
    pass;
