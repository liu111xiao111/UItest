# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.hui_life_page_configs import HuiLifePageConfigs

HLPC = HuiLifePageConfigs()

class HuiLifePage(SuperPage):
    '''
    This is hui life page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''
        super(HuiLifePage, self).__init__(testcase,
                                          driver,
                                          logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.text_activity_button,
                                          HLPC.assert_view_timeout)

    def clickOnActivity(self):
        '''
        usage: click on the activity button.
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_activity_button,
                                         HLPC.click_on_button_timeout);

    def clickOnPrivilege(self):
        '''
        usage: click on the privilege button.
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_privilege_button,
                                         HLPC.click_on_button_timeout);

    def clickOnSpecificActivity(self):
        '''
        usage: click on the specific activity button.
        '''
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_specific_activity_button,
                                       HLPC.click_on_button_timeout);

    def clickOnSpecificPrivilege(self):
        '''
        usage: click on the specific privilege button.
        '''
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_specific_privilege_button,
                                       HLPC.click_on_button_timeout);


    def clickOnResourceNiche(self):
        '''
        usage: click on resource niche.
        '''
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       HLPC.resource_id_resource_niche_button,
                                       HLPC.click_on_button_timeout)

    def clickOnExpressTrain(self):
        '''
        usage: click on express train
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_express_train,
                                         HLPC.click_on_button_timeout)

    def clickOnTaxi(self):
        '''
        usage: click on taxi
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_taxi,
                                         HLPC.click_on_button_timeout)

    def clickOnSpecialTrain(self):
        '''
        usage: click on special train
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_special_train,
                                         HLPC.click_on_button_timeout)

    def clickOnDesignatedDriving(self):
        '''
        usage: click on designated driving
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_designated_driving,
                                         HLPC.click_on_button_timeout)

    def clickOnFlyYue(self):
        '''
        usage: click on fly yue
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_fly_yue,
                                         HLPC.click_on_button_timeout)

    def clickOnPrepaidRecharge(self):
        '''
        usage: click on prepaid recharge
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_prepaid_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnTrafficRecharge(self):
        '''
        usage: click on traffic recharge
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_traffic_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnQQRecharge(self):
        '''
        usage: click on qq recharge
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_qq_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnOnlineGameRecharge(self):
        '''
        usage: click on online game recharge
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_online_game_recharge,
                                         HLPC.click_on_button_timeout)

    def clickOnStockInformation(self):
        '''
        usage: click on stock information
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         HLPC.text_stock_information,
                                         HLPC.click_on_button_timeout)

    def validDiDiTravel(self):
        '''
        usage: valid didi travel view
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              HLPC.verify_resource_didi_travel,
                                              HLPC.assert_view_timeout)

    def validFlyYue(self):
        '''
        usage: valid fly yue view
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_fly_yue,
                                          HLPC.assert_view_timeout)

    def validPrepaidRecharge(self):
        '''
        usage: valid prepaid recharge view
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_prepaid_recharge,
                                          HLPC.assert_view_timeout)

    def validTrafficRecharge(self):
        '''
        usage: valid traffic recharge view
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_traffic_recharge,
                                          HLPC.assert_view_timeout)

    def validQQRecharge(self):
        '''
        usage: valid qq recharge view
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_qq_recharge,
                                          HLPC.assert_view_timeout)

    def validOnlineGameRecharge(self):
        '''
        usage: valid online game recharge view
        '''
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          HLPC.verify_text_online_game_recharge,
                                          HLPC.assert_view_timeout)

    def validStockInformation(self):
        '''
        usage: valid stock information view
        '''
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  HLPC.verify_text_stock_information,
                                                  HLPC.assert_view_timeout)

    def validModules(self):
        '''
        usage: click on modules button and valid
        '''
        module_list = (# Express train
                       {"click" : self.clickOnExpressTrain,
                        "valid" : self.validDiDiTravel},
                       # Taxi
                       {"click" : self.clickOnTaxi,
                        "valid" : self.validDiDiTravel},
                       # Designated driving
                       {"click" : self.clickOnDesignatedDriving,
                        "valid" : self.validDiDiTravel},
                       # Special train
                       {"click" : self.clickOnSpecialTrain,
                        "valid" : self.validDiDiTravel},
                       # Fly yue
                       {"click" : self.clickOnFlyYue,
                        "valid" : self.validFlyYue},
                       # Prepaid recharge
                       {"click" : self.clickOnPrepaidRecharge,
                        "valid" : self.validPrepaidRecharge},
                       # Traffic recharge
                       {"click" : self.clickOnTrafficRecharge,
                        "valid" : self.validTrafficRecharge},
                       # QQ recharge
                       {"click" : self.clickOnQQRecharge,
                        "valid" : self.validQQRecharge},
                       # Online game recharge
                       {"click" : self.clickOnOnlineGameRecharge,
                        "valid" : self.validOnlineGameRecharge},
                       # Stock information
                       {"click" : self.clickOnStockInformation,
                        "valid" : self.validStockInformation})

        for module in module_list:
            module["click"]()
            module["valid"]()
            self.clickBackKey()

#         API().scroll_to_text(self.driver, self.logger, HuiLifePageConfigs.text_specific_activity_title)
#         API().click_view_by_xpath(self.testcase, self.driver, self.logger, HuiLifePageConfigs.xpath_specific_privilege_button, HuiLifePageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
