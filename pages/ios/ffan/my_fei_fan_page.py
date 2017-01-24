# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.my_fei_fan_page_configs import MyFeiFanPageConfigs
from pages.logger import logger

class MyFeiFanPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MyFeiFanPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''
        logger.info("Check 我的飞凡 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.resource_id_my_fei_fan_title_st,
                                  MyFeiFanPageConfigs.assert_view_timeout)
        logger.info("Check 我的飞凡 end")
        API().screenShot(self.driver,"woDeFeiFan")

    def validLoginStatus(self, assertable=True):
        '''
        usage: Verify whether the current status is login.
        '''
        logger.info("Check 登录状态 begin")
        if assertable:
            API().assertElementByName(self.testcase, self.driver, self.logger,
                                      MyFeiFanPageConfigs.resource_id_nickname_st,
                                      MyFeiFanPageConfigs.assert_view_timeout)
            return True
        else:
            return API().validElementByName(self.driver, self.logger,
                                            MyFeiFanPageConfigs.resource_id_nickname_st,
                                            MyFeiFanPageConfigs.assert_view_timeout)
        logger.info("Check 登录状态 end")
        API().screenShot(self.driver, "dengLuZhuangTai")

    def validLogoutStatus(self):
        '''
        usage: Verify whether the current status is logout.
        '''
        logger.info("Check 退出登录 begin")
        for _ in range(1):
            self.scrollAsScreenPercent(0.5, 0.4, 0.5, 0.6)
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.resource_id_login_bt,
                                  MyFeiFanPageConfigs.assert_view_timeout)
        logger.info("Check 退出登录 end")
        API().screenShot(self.driver, "tuiChuDengLu")

    def clickOnLogin(self):
        '''
        usage: click on the login button.
        '''
        logger.info("Click 登录 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_login_bt,
                                 MyFeiFanPageConfigs.assert_view_timeout)
        logger.info("Click 登录 end")

    def clickOnSettings(self):
        '''
        usage: click on the settings button.
        '''
        logger.info("Click 设置 begin")
        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_settings_st,
                                 MyFeiFanPageConfigs.click_on_button_timeout)
        logger.info("Click 设置 end")

    def clickOnMessageCentre(self):
        '''
        usage: click on the message centre button.
        '''
        logger.info("Click 消息中心 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.xpath_message_centre_bt,
                                  MyFeiFanPageConfigs.click_on_button_timeout)
        logger.info("Click 消息中心 end")

    def clickOnMembershipCardPackage(self):
        '''
        usage: click on the membership card package button.
        '''
        logger.info("Click 会员卡包 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.xpath_membership_card_package_st,
                                  MyFeiFanPageConfigs.click_on_button_timeout)
        logger.info("Click 会员卡包 end")

    def clickOnNickname(self):
        '''
        usage: click on the nickname button.
        '''
        logger.info("Click 会员名 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_nickname_st,
                                 MyFeiFanPageConfigs.click_on_button_timeout)
        logger.info("Click 会员名 begin")

    def clickOnMyFeiFanCard(self):
        '''
        usage: click on the my fei fan card button.
        '''
        logger.info("Click 我的飞凡通 begin")
        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_my_fei_fan_card_st,
                                 MyFeiFanPageConfigs.click_on_button_timeout)
        logger.info("Click 我的飞凡通 end")


if __name__ == '__main__':
    pass
