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

    def addPlateNumber(self):
        '''
        添加车牌
        :return:
        '''
        logger.info("Click 添加车牌 begin")

        #如果已经添加了,删除这个车牌
        isAlreadyAddPlateNumber = API().validElementByName(self.driver, self.logger, ParkingPageConfigs.text_plate_number)

        #print(isAlreadyAddPlateNumber)

        if not isAlreadyAddPlateNumber:
            pass

        else:

            #删除车牌,点击车牌号,显示出删除按钮
            API().clickElementByName(self.testcase,
                                     self.driver,
                                     self.logger,
                                     ParkingPageConfigs.text_plate_number)
            #点击删除按钮
            API().clickElementByXpath(self.testcase,
                                      self.driver,
                                      self.logger,
                                      ParkingPageConfigs.xpath_delete_plate_number)


        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  ParkingPageConfigs.xpath_delete_plate_number)
        logger.info("Click 添加车牌 end")


    def validPlateNumberPage(self):
        '''
        验证车牌管理页面
        :return:
        '''
        logger.info("Check 添加车牌 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  name=ParkingPageConfigs.name_add_plate_number)
        logger.info("Check 添加车牌 end")
        API().screenShot(self.driver, "tianJiaChePai")


    def inputPlateNumber(self):
        '''
        输入车牌号,自定义输入框,input方法无法输入,点击键盘输入
        :return:
        '''
        plateNumberArr = ["B","more, numbers","6","7","8","9","1"]


        logger.info("Input 车牌号 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger, ParkingPageConfigs.xpaht_plate_number_edit_text)

        #点击键盘输入
        for number in plateNumberArr:
            API().clickElementByName(self.testcase, self.driver, self.logger, number)


        logger.info("Input 车牌号 end")
        API().screenShot(self.driver, "chePaiHao")

    def clickOnEnsureButton(self):
        logger.info("Click 确定 begin")

        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 ParkingPageConfigs.name_enture_button)

        logger.info("Click 确定 end")


    def scrollToFujintingche(self):
        '''
        滑动到附近停车场
        :return:
        '''
        API().iosScrollToElement(self.driver,
                                 self.logger,
                                 "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAButton[1]",
                                 ParkingPageConfigs.name_nearby_parking)

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
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 ParkingPageConfigs.name_parking_coupon)
        logger.info("Click 停车券 end")

    def validTingchequan(self):
        logger.info("Check 停车券 begin")
        #暂保留, 用name方式,有时候可以验证成功,有时候无法抓取出页面信息
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  name=ParkingPageConfigs.name_parking_coupon_cn)

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
