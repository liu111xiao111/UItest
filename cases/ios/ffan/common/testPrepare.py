# -*- coding: utf-8 -*-

from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.login_page import LoginPage
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from pages.ios.ffan.switch_city_page import SwitchCityPage
from pages.ios.ffan.version_upgrade_page import VersionUpgradePage


class TestPrepare:

    def __init__(self, testcase, driver, logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def prepare(self, needLogin=True):
#         self.updateVersion()
        self.switchCity()
        self.dealActivities()

        if needLogin:
            self.login()
            self.backToDashBoard()

    def login(self):
        self.logger.info("Begin login")
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self.testcase, self.driver, self.logger)
        myFeiFanPage.validSelf()
        if myFeiFanPage.validLoginStatus(False):
            return
        myFeiFanPage.clickOnLogin()

        loginPage = LoginPage(self.testcase, self.driver, self.logger)
        loginPage.validSelf()
        loginPage.switchToNormalLogin()
        loginPage.inputUserName()
        loginPage.inputPassWord()
        loginPage.clickOnLoginBtn()
        loginPage.waitBySeconds(5)

        myFeiFanPage.validSelf()
        self.logger.info("End login")

    def updateVersion(self):
        versionUpgradePage = VersionUpgradePage(self.testcase, self.driver, self.logger)
        if versionUpgradePage.validSelf(False):
            versionUpgradePage.cancelVersionUpgrade()
            versionUpgradePage.waitBySeconds()

    def switchCity(self):
        self.logger.info("Cancel 城市切换 begin")
        switchCityPage = SwitchCityPage(self.testcase, self.driver, self.logger)
        if switchCityPage.validSelf(False):
            switchCityPage.cancelSwitchCity()
            switchCityPage.waitBySeconds()
        self.logger.info("Cancel 城市切换 end")

    def backToDashBoard(self):
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.clickOnBornToShop()

    def closeHomeShakeTips(self):
        dashboardPage = DashboardPage(testcase=self.testcase , driver=self.driver , logger=self.logger)
        dashboardPage.clickOnHomeShakeTips()


    def dealActivities(self):
        '''
         处理主页出现的活动页面,如果有活动页面将其删除
        :return:
        '''
        dashboardPage = DashboardPage(testcase=self.testcase, driver=self.driver, logger=self.logger)
        dashboardPage.dealAcitivities()


if __name__ == '__main__':
    pass
