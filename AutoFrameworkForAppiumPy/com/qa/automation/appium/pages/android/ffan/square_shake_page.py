# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_shake_page_configs import SquareShakePageConfigs as SSPC


class SquareShakePage(SuperPage):
    '''
    作者 乔佳溪
    广场＝>现场摇
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareShakePage, self).__init__(testcase , driver, logger)

    def validSelf(self):
        '''
        usage : 进入现场摇页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SSPC.resource_id_shake,
                                        SSPC.click_on_button_timeout)

    def clickShake(self):
        '''
        usage : 点击摇一摇
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SSPC.resource_id_shake,
                                       SSPC.click_on_button_timeout)

    def validShake(self):
        '''
        usage: 验证摇一摇
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SSPC.resource_id_shake,
                                        SSPC.click_on_button_timeout)
