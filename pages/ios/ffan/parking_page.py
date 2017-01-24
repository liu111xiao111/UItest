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
        
    def clickParkingManagement(self):
        '''
        usage: 点击"车牌管理".
        '''
        logger.info("Click 车牌管理 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 ParkingPageConfigs.name_plate_nmuber_management)
        logger.info("Click 车牌管理 end")
    
    def validParkingManagement(self):
        logger.info("Check 车牌管理 begin")

        API().assertElementByName(self.testcase, self.driver, self.logger, name=ParkingPageConfigs.name_plate_nmuber_management_ch)

        logger.info("Check 车牌管理 end")
        API().screenShot(self.driver, "chePaiGuanLi")
        
    def clickOnFujintingche(self):
        '''
        usage: 点击"附近停车场".
        '''
        logger.info("Click 附近停车场 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 ParkingPageConfigs.name_nearby_parking)
        logger.info("Click 附近停车场 end")
    
    def validFujintingche(self):
        logger.info("Check 附近停车场 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  name=ParkingPageConfigs.name_nearby_parking_cn)
        logger.info("Click 附近停车场 end")
        API().screenShot(self.driver, "fuJinTingChe")

    def clickOnTingchequan(self):
        '''
        usage: 点击"停车券".
        '''
        logger.info("Click 停车券 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  name=ParkingPageConfigs.name_parking_coupon)
        logger.info("Click 停车券 end")

    def validTingchequan(self):
        logger.info("Check 停车券 begin")
        #暂保留, 用name方式,有时候可以验证成功,有时候无法抓取出页面信息
        # API().assertElementByName(self.testcase, self.driver, self.logger,
        #                           name=ParkingPageConfigs.name_parking_coupon_cn)

        API().assertElementByXpath(self.testcase, self.driver, self.logger, ParkingPageConfigs.xpath_parking_coupon)

        logger.info("Check 停车券 ends")
        API().screenShot(self.driver, "tingCheQuan")
        
    def clickOnTingchejilu(self):
        '''
        usage: 点击"停车记录".
        '''
        logger.info("Click 停车记录 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 ParkingPageConfigs.name_parking_record)
        logger.info("Click 停车记录 end")

    def validTingchejilu(self):
        logger.info("Check 停车记录 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  name=ParkingPageConfigs.name_parking_record_cn)
        logger.info("Check 停车记录 end")
        API().screenShot(self.driver, "tingCheJilu")
    
    def clickOnHelp(self):
        '''
        usage: 点击"帮助".
        '''
        logger.info("Click 帮助 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 ParkingPageConfigs.name_parking_help)
        logger.info("Click 帮助 end")

    def validHelp(self):
        logger.info("Check 帮助 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  name=ParkingPageConfigs.name_parking_help_ch)
        logger.info("Check 帮助 end")
        API().screenShot(self.driver, "bangZhu")

if __name__ == '__main__':
    pass;
