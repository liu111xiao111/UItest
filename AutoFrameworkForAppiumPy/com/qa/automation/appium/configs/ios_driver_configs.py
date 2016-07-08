# -*- coding: utf-8 -*-

from __init__ import *

from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil

class IosDriverConfigs(object):
    '''
    This is a configuration class for AppiumDriver class.
    '''

    platformName = "iOS"

    platformVersion = DeviceInfoUtil().get_product_version()

    deviceName = "iPhone"

    bundleId = "com.dianshang.wanhui"

    udid = DeviceInfoUtil().getUdid()

    driverUrl = "http://localhost:4723/wd/hub"

    def __init__(self):
        pass
