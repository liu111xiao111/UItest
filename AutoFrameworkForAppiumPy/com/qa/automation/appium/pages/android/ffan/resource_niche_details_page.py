# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.resource_niche_details_page_configs import ResourceNicheDetailsPageConfigs as RNDPC


class ResourceNicheDetailsPage(SuperPage):
    '''
    作者 陈诚
    首页=>广场=>资源位界面
    '''
    def __init__(self, testcase, driver, logger):
        super(ResourceNicheDetailsPage, self).__init__(testcase,
                                                       driver,
                                                       logger)

    def validSelf(self):
        '''
        usage: 验证资源位界面
        '''
        API().assertElementByClassName(self.testcase,
                                       self.driver,
                                       self.logger,
                                       RNDPC.class_name_android_webkit_WebView,
                                       90)
