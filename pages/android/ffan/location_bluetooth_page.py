# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.location_bluetooth_page_configs import LocationBluetoothPageConfigs as LBPC
from pages.logger import logger

class LocationBluetoothPage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>室内地图=>是否开启蓝牙设置提示
    '''
    def __init__(self, testcase, driver, logger):
        super(LocationBluetoothPage, self).__init__(testcase, driver, logger);

    def clickOnCancleBtn(self):
        '''
        usage : 点击 "取消"
        '''
        logger.info("Click (蓝牙未开启)取消 begin")
        cancel_btn = API().validElementByResourceId(self.driver,
                                                    self.logger,
                                                    LBPC.resource_id_cancle_button,
                                                    10)
        if cancel_btn:
            cancel_btn.click()
        logger.info("Click (蓝牙未开启)取消 end")

