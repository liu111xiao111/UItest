# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.hui_life_page_configs import HuiLifePageConfigs

HLPC = HuiLifePageConfigs()

class HuiLifePage(SuperPage):
    '''
    首页->惠生活页面
    '''

    def __init__(self, testcase, driver, logger):
        super(HuiLifePage, self).__init__(testcase,
                                          driver,
                                          logger)

    def validSelf(self):
        '''
        usage: 验证惠生活界面
        '''
        bottom_bar = API().get_view_by_resourceID(driver=self.driver, logger=self.driver, resource_id=HLPC.resource_id_ll_bottom_bar)
        framell_list = API().find_views_of_view_by_class_name_both(element=bottom_bar,logger=self.logger , driver=self.driver,className=HLPC.class_name_android_widget_FrameLayout)
        API().assert_equal(test_case = self.testcase, driver = self.logger, logger = self.logger, actual_text = framell_list[1].get_attribute("selected"), expect_text = "true")

    def clickOnActivity(self):
        '''
        usage: 点击活动
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_activity_button,
                                         HLPC.click_on_button_timeout);

    def clickOnPrivilege(self):
        '''
        usage: 点击优惠
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_privilege_button,
                                         HLPC.click_on_button_timeout);

    def clickOnSpecificActivity(self):
        '''
        usage: 点击特别活动按钮
        '''
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_specific_activity_button,
                                       HLPC.click_on_button_timeout);

    def clickOnSpecificPrivilege(self):
        '''
        usage: 点击特权
        '''
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_specific_privilege_button,
                                       HLPC.click_on_button_timeout);


    def clickOnResourceNiche(self):
        '''
        usage: 点击资源位
        '''
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_resource_niche_button,
                                       HLPC.click_on_button_timeout)

    def clickOnTaxi(self):
        '''
        usage: 点击打车
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_taxi,
                                         HLPC.click_on_button_timeout)

    def clickOnDesignatedDriving(self):
        '''
        usage: 点击代驾
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_designated_driving,
                                         HLPC.click_on_button_timeout)

    def clickOnBus(self):
        '''
        usage: 点击公交查询
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_bus,
                                         HLPC.click_on_button_timeout)

    def clickOnFeifanRead(self):
        '''
        usage: 点击飞凡阅读
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_feifan_read,
                                         HLPC.click_on_button_timeout)

    def clickOnFlyYue(self):
        '''
        usage: 点击飞悦
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_fly_yue,
                                         HLPC.click_on_button_timeout)

    def clickOnPrepaidRecharge(self):
        '''
        usage: 点击话费充值
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_prepaid_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnTrafficRecharge(self):
        '''
        usage: 点击流量充值
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_traffic_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnQQRecharge(self):
        '''
        usage: 点击QQ充值
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_qq_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnOnlineGameRecharge(self):
        '''
        usage: 点击网游充值
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_online_game_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnStockInformation(self):
        '''
        usage: 点击股票资讯
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_stock_information,
                                         HLPC.click_on_button_timeout)

    def clickOnRefuel(self):
        '''
        usage: 点击加油
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_refuel,
                                         HLPC.click_on_button_timeout)

    def clickOnConcert(self):
        '''
        usage: 点击演唱会
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_concert,
                                         HLPC.click_on_button_timeout)

    def clickOnDrama(self):
        '''
        usage: 点击话剧
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_drama,
                                         HLPC.click_on_button_timeout)

    def clickOnPhilharmonic(self):
        '''
        usage: 点击音乐会
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_philharmonic,
                                         HLPC.click_on_button_timeout)

    def clickOnIllegalInquiry(self):
        '''
        usage: 点击违章查询
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_illegal_inquiry,
                                         HLPC.click_on_button_timeout)

    def validDiDiTravel(self):
        '''
        usage: 验证滴滴出行界面
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              HLPC.verify_resource_didi_travel,
                                              HLPC.assert_view_timeout)

    def validFeifanRead(self):
        '''
        usage: 验证飞凡阅读界面
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_feifan_read,
                                          HLPC.assert_view_timeout)

    def validFlyYue(self):
        '''
        usage: 验证飞悦界面
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_fly_yue,
                                          HLPC.assert_view_timeout)

    def validPrepaidRecharge(self):
        '''
        usage: 验证话费充值界面
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_prepaid_recharge,
                                          HLPC.assert_view_timeout)

    def validTrafficRecharge(self):
        '''
        usage: 验证流量充值界面
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_traffic_recharge,
                                          HLPC.assert_view_timeout)

    def validQQRecharge(self):
        '''
        usage: 验证QQ充值界面
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_qq_recharge,
                                          HLPC.assert_view_timeout)

    def validOnlineGameRecharge(self):
        '''
        usage: 验证网游充值界面
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_online_game_recharge,
                                          HLPC.assert_view_timeout)

    def validStockInformation(self):
        '''
        usage: 验证股票资讯界面
        '''
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  HLPC.verify_text_stock_information,
                                                  HLPC.assert_view_timeout)

    def validRefuel(self):
        '''
        usage: 验证加油界面
        '''
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  HLPC.verify_text_refuel,
                                                  HLPC.assert_view_timeout)

    def validConcert(self):
        '''
        usage: 验证演唱会界面
        '''
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  HLPC.verify_text_concert,
                                                  HLPC.assert_view_timeout)

    def validDrama(self):
        '''
        usage: 验证话剧界面
        '''
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  HLPC.verify_text_drama,
                                                  HLPC.assert_view_timeout)

    def validPhilharmonic(self):
        '''
        usage: 验证音乐会界面
        '''
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  HLPC.verify_text_philharmonic,
                                                  HLPC.assert_view_timeout)

    def validIllegalInquiry(self):
        '''
        usage: 验证违章查询界面
        '''
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  HLPC.verify_text_illegal_inquiry,
                                                  HLPC.assert_view_timeout)

if __name__ == '__main__':
    pass
