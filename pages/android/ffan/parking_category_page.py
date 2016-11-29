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
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        PCPC.resource_id_tv_parking_tv,
                                        30)
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
                                 10)
        return vehiclePlate
        logger.info("Check 车牌是否已添加 end")

    def clickOnAddLicensePlate(self):
        '''
        usage : 点击添加车牌
        '''
        logger.info("Click 添加车牌 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PCPC.text_add_license_plate,
                                 10)
        logger.info("Click 添加车牌 end")
