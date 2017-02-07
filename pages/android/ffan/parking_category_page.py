# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.parking_category_page_configs import ParkingCategoryPageConfigs as PCPC
from pages.logger import logger


class ParkingCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车
    '''
    def __init__(self,testcase,driver,logger):
        super(ParkingCategoryPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 验证停车页面
        '''
        logger.info("Check 停车页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  PCPC.text_parking,
                                  PCPC.valid_timeout)
        logger.info("Check 停车页面 end")

    def clickOnParkingLot(self):
        '''
        usage : 点击附近停车场
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       PCPC.resource_id_tv_parking_lot_tv,
                                       10)

    def clickOnParkingPayment(self):
        '''
        usage : 点击停车缴费
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       PCPC.resource_id_tv_parking_payment_tv,
                                       10)

    def validVehiclePlateExist(self):
        '''
        usage : 判断车牌是否已添加
        '''
        logger.info("Check 车牌是否已添加 begin")
        vehiclePlate = API().validElementByText(self.driver,
                                 self.logger,
                                 PCPC.text_add_license_plate,
                                 30)
        if vehiclePlate != False:
            logger.info("Check 车牌未添加 end")
        else:
            logger.info("Check 车牌已添加 end")
        logger.info("Check 车牌是否已添加 end")
        return vehiclePlate

    def clickOnAddLicensePlate(self):
        '''
        usage : 点击添加车牌
        '''
        logger.info("Click 添加车牌 begin")
#         API().clickElementByText(self.testcase,
#                                  self.driver,
#                                  self.logger,
#                                  PCPC.text_add_license_plate,
#                                  10)
        API().clickElementByXpath(self.testcase,
                                self.driver,
                                self.logger,
                                PCPC.xpath_add_license_plate,
                                60)
        logger.info("Click 添加车牌 end")
