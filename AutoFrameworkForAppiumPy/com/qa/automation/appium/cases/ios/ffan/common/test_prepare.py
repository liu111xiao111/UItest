# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.login_page import LoginPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.ios.ffan.switch_city_page import SwitchCityPage
from com.qa.automation.appium.pages.ios.ffan.version_upgrade_page import VersionUpgradePage


class TestPrepare:

    def __init__(self, testcase, driver, logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def prepare(self, needLogin=True):
#         self.updateVersion()
        self.switchCity()

        if needLogin:
            self.login()
            self.backToDashBoard()

    def login(self):
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

    def updateVersion(self):
        versionUpgradePage = VersionUpgradePage(self.testcase, self.driver, self.logger)
        if versionUpgradePage.validSelf(False):
            versionUpgradePage.cancelVersionUpgrade()
            versionUpgradePage.waitBySeconds()

    def switchCity(self):
        switchCityPage = SwitchCityPage(self.testcase, self.driver, self.logger)
        if switchCityPage.validSelf(False):
            switchCityPage.cancelSwitchCity()
            switchCityPage.waitBySeconds()

    def backToDashBoard(self):
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.clickOnBornToShop()

    def closeHomeShakeTips(self):
        dashboardPage = DashboardPage(testcase=self.testcase , driver=self.driver , logger=self.logger)
        dashboardPage.clickOnHomeShakeTips()

if __name__ == '__main__':
    pass
