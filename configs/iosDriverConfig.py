# -*- coding: utf-8 -*-


from utility.device_info_util import DeviceInfoUtil

class IosDriverConfigs(object):
    '''
    This is a configuration class for AppiumDriver class.
    '''

    platformName = "iOS"

  #  platformVersion = DeviceInfoUtil().getIProductVersion()
    platformVersion = 'iPhone5s'

    deviceName = "iPhone5s"

    bundleId = "com.dianshang.wanhui"

    #商户
    bundleId_sh = "com.dianshang.feifanbp"

   # udid = DeviceInfoUtil().getUdid()
    udid = 'af8b9ab2f006968724115ea516fa19b268e94a3d'

    driverUrl = "http://localhost:4723/wd/hub"

    def __init__(self):
        pass
