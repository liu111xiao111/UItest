# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.general_coupon_page_configs import GeneralCouponPageConfigs


class GeneralCouponPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>通用券
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(GeneralCouponPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  GeneralCouponPageConfigs.resource_id_general_coupon_title,
                                  GeneralCouponPageConfigs.assert_view_timeout)

    def clickOnImmediatelyToReceive(self):
        '''
        usage: click on the immediately to receive button.
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  GeneralCouponPageConfigs.xpath_immediately_to_receive,
                                  GeneralCouponPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
