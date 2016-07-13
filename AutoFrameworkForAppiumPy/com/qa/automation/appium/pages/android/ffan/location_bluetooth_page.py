# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.location_bluetooth_page_configs import LocationBluetoothPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from selenium.common.exceptions import TimeoutException

class LocationBluetoothPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LocationBluetoothPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : Click "取消"
    '''

    def clickOnCancleBtn(self):
        try:
            cancel_btn = API().find_view_by_resourceID_Until_android(driver=self.driver, logger=self.logger,
                                           resource_id=LocationBluetoothPageConfigs.resource_id_cancle_button, seconds=3)
            if cancel_btn:
                cancel_btn.click()
        except TimeoutException as exc:
            print("except ",exc)
            pass;
#             

if __name__ == '__main__':
    pass;