# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.hui_life_page_configs import HuiLifePageConfigs

HLPC = HuiLifePageConfigs()


class HuiLifePage(SuperPage):
    '''
    作者 宋波
    首页=>惠生活页面
    '''

    def __init__(self, testcase, driver, logger):
        super(HuiLifePage, self).__init__(testcase,
                                          driver,
                                          logger)

    def validSelf(self):
        '''
        usage: 验证惠生活界面
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  HuiLifePageConfigs.resource_id_taking_taxi_st,
                                  HuiLifePageConfigs.assert_view_timeout)

    def clickOnAndValidByXpathAndName(self, viewXpath, validValue):
        '''
        usage: 点击一个控件，并验证是否点击正确。
        '''

        print("KEYWORDS: %s" % validValue)
        API().clickElementByXpath(self.testcase, self.driver, self.logger, viewXpath,
                                  HuiLifePageConfigs.click_on_button_timeout)
        API().waitBySeconds(10)
        if u"加油" == validValue:
            # API.assertElementByXpath(self.testcase,self.driver,self.logger,
            #                          "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[1]")
            API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                       HuiLifePageConfigs.xpath_jiayou,
                                       HuiLifePageConfigs.assert_view_timeout)
        else:
            API().assertElementByName(self.testcase, self.driver, self.logger, validValue,
                                              HuiLifePageConfigs.assert_view_timeout)
        if u"滴滴出行" == validValue:
            tempXpath = "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]"
        else:
            tempXpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]"

        API().clickBackKeyForIos(self.testcase, self.driver, self.logger, tempXpath,
                                 HuiLifePageConfigs.click_on_button_timeout)

    def clickOnActivity(self):
        '''
        usage: 点击活动
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_activity_button,
                                 HLPC.click_on_button_timeout);

    def clickOnPrivilege(self):
        '''
        usage: 点击优惠
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_privilege_button,
                                 HLPC.click_on_button_timeout);

    def clickOnSpecificActivity(self):
        '''
        usage: 点击特别活动按钮
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.resource_id_specific_activity_button,
                                 HLPC.click_on_button_timeout);

    def clickOnSpecificPrivilege(self):
        '''
        usage: 点击特权
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.resource_id_specific_privilege_button,
                                 HLPC.click_on_button_timeout);


    def clickOnResourceNiche(self):
        '''
        usage: 点击资源位
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.resource_id_resource_niche_button,
                                 HLPC.click_on_button_timeout)

    def clickOnTaxi(self):
        '''
        usage: 点击打车
        '''
        API().clickElementByText(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_taxi,
                                         HLPC.click_on_button_timeout)


    def clickOnJingxuan(self):
        '''
        usage: 点击精选,验证精选页面加载
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.name_jingxuan,
                                 HLPC.click_on_button_timeout)

        API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                   HuiLifePageConfigs.xpath_jingxuan_title,
                                   HuiLifePageConfigs.assert_view_timeout)

    def clickOnJiandian(self):
        '''
        usage: 点击推荐店,验证精选页面加载
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.name_jiandian,
                                 HLPC.click_on_button_timeout)

        API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                   HuiLifePageConfigs.xpath_jiandian_title,
                                   HuiLifePageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
