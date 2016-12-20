# -*- coding: utf-8 -*-

import time
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.parking_add_license_plate_page_configs import ParkingAddLicensePlatePageConfigs as PALPPC
from api.logger import logger


class ParkingAddLicensePlatePage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费
    '''
    def __init__(self,testcase,driver,logger):
        super(ParkingAddLicensePlatePage, self).__init__(testcase, driver, logger);


    def validSelf(self):
        '''
        usage : 判断“添加车牌”是否正确显示
        '''
        logger.info("Check 添加车牌页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        PALPPC.resource_id_tv_parking_payment_tv,
                                        90)
        logger.info("Check 添加车牌页面 end")

    def inputVIN(self):
        '''
        usage : 输入车牌号
        '''
        logger.info("Input 车牌号 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      PALPPC.resource_id_tv_VIN_tv,
                                      PALPPC.input_VIN,
                                      90)
        logger.info("Input 车牌号 end")

    def clickOnConfirmBtn(self):
        '''
        usage: 点击"确定"
        '''
        logger.info("Click 确定 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PALPPC.text_confirm_btn,
                                 60)
        logger.info("Click 确定 end")

    def clickAndValidItems(self, item = "default", title = "default"):
        '''
        usage: 点击各入口项目
        '''
        logger.info("Check 入口项目 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 item,
                                 90)
        API().waitBySeconds(2)
        API().screenShot(self.driver, "tingCheRuKou")
        notice = API().validElementByXpath(self.driver, self.logger, PALPPC.xpath_notice, 10)
        if not notice:
            API().assertElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 title,
                                 60)
            API().clickBackKeyForAndroid(self.driver, self.logger)
            API().screenShot(self.driver, "tingChe")
        else:
            API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     PALPPC.text_know,
                                     60)
        logger.info("Check 入口项目 end")

    def validManager(self):
        '''
        usage : 判断“车牌管理”是否正确显示
        '''
        logger.info("Check 车牌管理页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        PALPPC.resource_id_tv_parking_manager_tv,
                                        90)
        logger.info("Check 车牌管理页面 end")

    def clickOnVehicleManager(self):
        '''
        usage : 点击“车牌管理”
        '''
        logger.info("Click 车牌管理 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PALPPC.text_vehicle_manager,
                                 90)
        logger.info("Click 车牌管理 end")

    def clickOnVehiclePlate(self):
        '''
        usage : 点击车牌
        '''
        logger.info("Click 车辆 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       PALPPC.resource_id_tv_vehicle_plate,
                                       90)
        logger.info("Click 车辆 end")

    def clickOnDeleteVehiclePlate(self):
        '''
        usage : 点击“删除车牌”
        '''
        logger.info("Click 删除车牌 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PALPPC.text_delete_vehicle_plate,
                                 90)
        logger.info("Click 删除车牌 end")

