# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.ffan.parking_page_configs import ParkingPageConfigs
from pages.ios.common.superPage import SuperPage
from pages.logger import logger

class ParkingPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车
    '''

    def __init__(self, testcase, driver, logger):
        super(ParkingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        logger.info("Check 停车 begin")
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
        logger.info("Check 停车 end")
        API().screenShot(self.driver, "tingChe")

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
        logger.info("Click 找车 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchezhaoche,
                                  ParkingPageConfigs.click_on_button_timeout)
        logger.info("Click 找车 end")
    
    def validZhaoche(self):
        logger.info("Check 找车 begin")
        notFindGpsSquare = API().validElementByName(self.driver, self.logger, ParkingPageConfigs.name_not_gps_square)
        if notFindGpsSquare == False:
            API().assertElementByIosUiautomation(self.testcase,self.driver,self.logger
                 ,uiaString=".navigationBars()[0]")
            self.clickBackKey()
        else:
            API().clickElementByName(self.testcase, self.driver, self.logger, ParkingPageConfigs.name_know_text)
        logger.info("Check 找车 end")
        API().screenShot(self.driver, "zhaoChe")
        
    def clickOnFujintingche(self):
        '''
        usage: 点击"附近停车场".
        '''
        logger.info("Click 附近停车场 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_fujintingchechang,
                                  ParkingPageConfigs.click_on_button_timeout)
        logger.info("Click 附近停车场 end")
    
    def validFujintingche(self):
        logger.info("Check 附近停车场 begin")
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
        logger.info("Click 附近停车场 end")
        API().screenShot(self.driver, "fuJinTingChe")

    def clickOnTingchequan(self):
        '''
        usage: 点击"停车券".
        '''
        logger.info("Click 停车券 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchequan,
                                  ParkingPageConfigs.click_on_button_timeout)
        logger.info("Click 停车券 end")

    def validTingchequan(self):
        logger.info("Check 停车券 begin")
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
        logger.info("Check 停车券 ends")
        API().screenShot(self.driver, "tingCheQuan")
        
    def clickOnTingchejilu(self):
        '''
        usage: 点击"停车记录".
        '''
        logger.info("Click 停车记录 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_tingchejilu,
                                  ParkingPageConfigs.click_on_button_timeout)
        logger.info("Click 停车记录 end")

    def validTingchejilu(self):
        logger.info("Check 停车记录 begin")
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
        logger.info("Check 停车记录 end")
        API().screenShot(self.driver, "tingCheJilu")
    
    def clickOnHelp(self):
        '''
        usage: 点击"帮助".
        '''
        logger.info("Click 帮助 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ParkingPageConfigs.xpath_bangzhu,
                                  ParkingPageConfigs.click_on_button_timeout)
        logger.info("Click 帮助 end")

    def validHelp(self):
        logger.info("Check 帮助 begin")
        API().assertElementByIosUiautomation(self.testcase, self.driver, self.logger
                                             , uiaString=".navigationBars()[0]")
        logger.info("Check 帮助 end")
        API().screenShot(self.driver, "bangZhu")

if __name__ == '__main__':
    pass;
