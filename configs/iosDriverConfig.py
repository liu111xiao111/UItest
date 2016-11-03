# -*- coding: utf-8 -*-


from utility.device_info_util import DeviceInfoUtil

class IosDriverConfigs(object):
    '''
    This is a configuration class for AppiumDriver class.
    '''

    platformName = "iOS"

    platformVersion = DeviceInfoUtil().get_product_version()

    deviceName = "iPhone6s"

    bundleId = "com.dianshang.wanhui"

    #商户
    bundleId_sh = "com.dianshang.feifanbp"

    udid = DeviceInfoUtil().getUdid()

    driverUrl = "http://localhost:4723/wd/hub"

    def __init__(self):
        pass
