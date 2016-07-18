# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.login_page import LoginPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.ios.ffan.switch_city_page import SwitchCityPage
from com.qa.automation.appium.pages.ios.ffan.version_upgrade_page import VersionUpgradePage

'''
    usage :
'''
class TestPrepare:

    def __init__(self, testcase, driver, logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def prepare(self, needLogin=True):
        self.updateVersion()
        self.switchCity()

        # self.closeHomeShakeTips()

        if needLogin == True:
            self.login()

        self.backToDashBoard()

    def login(self):
        dashboardPage = DashboardPage(testcase=self.testcase , driver=self.driver , logger=self.logger)
        myFfanPage = MyFfanPage(testcase=self.testcase, driver=self.driver, logger=self.logger)

        dashboardPage.click_my()
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(testcase=self.testcase, driver=self.driver, logger=self.logger)
        loginPage.validSelf()
        # loginPage.waitBySeconds(seconds=2)
        loginPage.switchToNormalLogin()
        loginPage.inputUserName();
        # loginPage.waitBySeconds(seconds=1)
        loginPage.inputPassWord()
        # loginPage.waitBySeconds(seconds=1)
        loginPage.clickOnLoginBtn();
        # loginPage.waitBySeconds(seconds=3)
        # dashboardPage.validSelf()
        # dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        # myFfanPage.validLoginStatus()
        dashboardPage.waitBySeconds(seconds=2);


    def updateVersion(self):
        versionUpgradePage = VersionUpgradePage(self.testcase, self.driver, self.logger)
        tempTimes = 0
        while versionUpgradePage.validSelf(False) and tempTimes < 3:
            versionUpgradePage.cancelVersionUpgrade()
            versionUpgradePage.waitBySeconds()
            tempTimes += 1
        # versionUpgradePage.invalidSelf()

    def switchCity(self):
        switchCityPage = SwitchCityPage(self.testcase, self.driver, self.logger)
        tempTimes = 0
        while switchCityPage.validSelf(False) and tempTimes < 3:
            switchCityPage.cancelSwitchCity()
            switchCityPage.waitBySeconds()
            tempTimes += 1
            # switchCityPage.invalidSelf()

    def backToDashBoard(self):
        dashboardPage = DashboardPage(testcase=self.testcase , driver=self.driver , logger=self.logger)
        dashboardPage.click_aiguangjie()


    def closeHomeShakeTips(self):
        dashboardPage = DashboardPage(testcase=self.testcase , driver=self.driver , logger=self.logger)
        dashboardPage.clickOnHomeShakeTips()

if __name__ == '__main__':
    pass;
