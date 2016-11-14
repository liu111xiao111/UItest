# -*- coding:utf-8 -*-

import logging

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.hui_life_page_configs import HuiLifePageConfigs as HLPC
from pages.logger import logger


class HuiLifePage(SuperPage):
    '''
    作者 宋波
    首页=>惠生活页面
    '''
    def __init__(self, testcase, driver, logger):
        super(HuiLifePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证慧生活界面
        '''
        logger.info("Check 慧生活页面 begin")
        API().assertElementsByTexts(self.testcase, self.driver, self.logger,
                                    HLPC.text_valid_content, HLPC.assert_view_timeout)
        logger.info("Check 慧生活页面 end")

    def clickOnActivity(self):
        '''
        usage: 点击活动
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_activity_button,
                                 HLPC.click_on_button_timeout)

    def clickOnPrivilege(self):
        '''
        usage: 点击优惠
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_privilege_button,
                                 HLPC.click_on_button_timeout)

    def clickOnSpecificActivity(self):
        '''
        usage: 点击特别活动按钮
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_specific_activity_button,
                                       HLPC.click_on_button_timeout)

    def clickOnSpecificPrivilege(self):
        '''
        usage: 点击特权
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_specific_privilege_button,
                                       HLPC.click_on_button_timeout);


    def clickOnResourceNiche(self):
        '''
        usage: 点击资源位
        '''
        API().clickElementByResourceId(self.testcase,
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

    def clickOnDesignatedDriving(self):
        '''
        usage: 点击代驾
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_designated_driving,
                                 HLPC.click_on_button_timeout)

    def clickOnBus(self):
        '''
        usage: 点击公交查询
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_bus,
                                 HLPC.click_on_button_timeout)

    def clickOnFeifanRead(self):
        '''
        usage: 点击飞凡阅读
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_feifan_read,
                                 HLPC.click_on_button_timeout)

    def clickOnFlyYue(self):
        '''
        usage: 点击飞悦
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_fly_yue,
                                 HLPC.click_on_button_timeout)

    def clickOnPrepaidRecharge(self):
        '''
        usage: 点击话费充值
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_prepaid_recharge,
                                 HLPC.click_on_button_timeout)

    def clickOnTrafficRecharge(self):
        '''
        usage: 点击流量充值
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_traffic_recharge,
                                 HLPC.click_on_button_timeout)

    def clickOnQQRecharge(self):
        '''
        usage: 点击QQ充值
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_qq_recharge,
                                 HLPC.click_on_button_timeout)

    def clickOnOnlineGameRecharge(self):
        '''
        usage: 点击网游充值
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_online_game_recharge,
                                 HLPC.click_on_button_timeout)

    def clickOnStockInformation(self):
        '''
        usage: 点击股票资讯
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_stock_information,
                                 HLPC.click_on_button_timeout)

    def clickOnRefuel(self):
        '''
        usage: 点击加油
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_refuel,
                                 HLPC.click_on_button_timeout)

    def clickOnConcert(self):
        '''
        usage: 点击演唱会
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_concert,
                                 HLPC.click_on_button_timeout)

    def clickOnDrama(self):
        '''
        usage: 点击话剧
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_drama,
                                 HLPC.click_on_button_timeout)

    def clickOnPhilharmonic(self):
        '''
        usage: 点击音乐会
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_philharmonic,
                                 HLPC.click_on_button_timeout)

    def clickOnIllegalInquiry(self):
        '''
        usage: 点击违章查询
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_illegal_inquiry,
                                 HLPC.click_on_button_timeout)

    def validDiDiTravel(self):
        '''
        usage: 验证滴滴出行界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        HLPC.verify_resource_didi_travel,
                                        HLPC.assert_view_timeout)

    def validFeifanRead(self):
        '''
        usage: 验证飞凡阅读界面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  HLPC.verify_text_feifan_read,
                                  HLPC.assert_view_timeout)

    def validFlyYue(self):
        '''
        usage: 验证飞悦界面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  HLPC.verify_text_fly_yue,
                                  HLPC.assert_view_timeout)

    def validPrepaidRecharge(self):
        '''
        usage: 验证话费充值界面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  HLPC.verify_text_prepaid_recharge,
                                  HLPC.assert_view_timeout)

    def validTrafficRecharge(self):
        '''
        usage: 验证流量充值界面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  HLPC.verify_text_traffic_recharge,
                                  HLPC.assert_view_timeout)

    def validQQRecharge(self):
        '''
        usage: 验证QQ充值界面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  HLPC.verify_text_qq_recharge,
                                  HLPC.assert_view_timeout)

    def validOnlineGameRecharge(self):
        '''
        usage: 验证网游充值界面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  HLPC.verify_text_online_game_recharge,
                                  HLPC.assert_view_timeout)

    def validStockInformation(self):
        '''
        usage: 验证股票资讯界面
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.verify_text_stock_information,
                                         HLPC.assert_view_timeout)

    def validRefuel(self):
        '''
        usage: 验证加油界面
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.verify_text_refuel,
                                         HLPC.assert_view_timeout)

    def validConcert(self):
        '''
        usage: 验证演唱会界面
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.verify_text_concert,
                                         HLPC.assert_view_timeout)

    def validDrama(self):
        '''
        usage: 验证话剧界面
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.verify_text_drama,
                                         HLPC.assert_view_timeout)

    def validPhilharmonic(self):
        '''
        usage: 验证音乐会界面
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.verify_text_philharmonic,
                                         HLPC.assert_view_timeout)

    def validIllegalInquiry(self):
        '''
        usage: 验证违章查询界面
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.verify_text_illegal_inquiry,
                                         HLPC.assert_view_timeout)

    def clickOnAndValidByXpathAndName(self, viewXpath, validValue):
        '''
        usage: 点击一个控件，并验证是否点击正确。
        '''
        logging.info("KEYWORDS: %s" % validValue)
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  viewXpath, HLPC.click_on_button_timeout)
        API().waitBySeconds(10)
        if (viewXpath == HLPC.xpath_optional_stock or viewXpath == HLPC.xpath_come_on):
            API().assertElementByContentDesc(self.testcase,
                                             self.driver,
                                             self.logger,
                                             validValue,
                                             HLPC.assert_view_timeout)
        else:
            API().assertElementByText(self.testcase,
                                      self.driver,
                                      self.logger,
                                      validValue,
                                      HLPC.assert_view_timeout)
        API().clickBackKeyForAndroid(self.driver, self.logger)

    def clickOnSelect(self):
        '''
        usage: 点击精选
        '''
        logger.info("Click 精选 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_select_button,
                                 HLPC.click_on_button_timeout)
        logger.info("Click 精选 end")

    def validSelfSelect(self):
        '''
        usage: 验证精选
        '''
        logger.info("Check 精选 begin")
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(2):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        HLPC.resource_id_select,
                                        HLPC.assert_view_timeout)
        logger.info("Check 精选 end")

    def clickOnSelectDetails(self):
        '''
        usage: 点击精选详细
        '''
        logger.info("Click 精选详细内容 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_select,
                                       HLPC.click_on_button_timeout)
        logger.info("Click 精选详细内容 end")

    def validSelfSelectDetails(self):
        '''
        usage: 验证精选详细页
        '''
        logger.info("Check 精选详细内容 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        HLPC.resource_id_select_details,
                                        HLPC.assert_view_timeout)
        logger.info("Check 精选详细内容 end")

    def clickOnShop(self):
        '''
        usage: 点击荐店
        '''
        logger.info("Click 荐店 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 HLPC.text_shop_button,
                                 HLPC.click_on_button_timeout)
        logger.info("Click 荐店 end")

    def validSelfShop(self):
        '''
        usage: 验证荐店
        '''
        logger.info("Check 荐店 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        HLPC.resource_id_select,
                                        HLPC.assert_view_timeout)
        logger.info("Check 荐店 end")

    def clickOnShopDetails(self):
        '''
        usage: 点击荐店详细
        '''
        logger.info("Click 荐店详细内容 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_select,
                                       HLPC.click_on_button_timeout)
        logger.info("Click 荐店详细内容 end")

    def validSelfShopDetails(self):
        '''
        usage: 验证荐店详细页
        '''
        logger.info("Check 荐店详细内容 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        HLPC.resource_id_select_details,
                                        HLPC.assert_view_timeout)
        logger.info("Check 荐店详细内容 end")
