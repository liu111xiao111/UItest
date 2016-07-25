# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.switch_city_page import SwitchCityPage
from com.qa.automation.appium.pages.android.ffan.version_upgrade_page import VersionUpgradePage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.login_page import LoginPage
from com.qa.automation.appium.pages.android.ffan.settings_page import SettingsPage


class TestPrepare:
    '''
    usage: 初始化配置方法
    '''
    def __init__(self, testcase, driver, logger):
        '''
        初始化方法
        '''
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def prepare(self, needLogin=True):
        '''
        usage: 测试前准备方法，移除更新和选择城市弹出框，并且根据选择判断是否需要登录
        '''
        self.updateVersion()
        self.switchCity()

        #self.closeHomeShakeTips()

        if needLogin == True:
            self.login()
        
        self.backToDashBoard()

    def login(self):
        '''
        usage: 登录方法
        '''
        dashboardPage = DashboardPage(self.testcase , self.driver , self.logger)
        myFfanPage = MyFfanPage(self.testcase, self.driver, self.logger)

        dashboardPage.clickOnMy()
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(self.testcase, self.driver, self.logger)
        loginPage.validSelf()
        loginPage.switchToNormalLogin()
        loginPage.inputUserName()
        loginPage.inputPassWord()
        loginPage.clickOnLoginBtn()
        myFfanPage.validSelf()
        dashboardPage.waitBySeconds(seconds=2);

    def updateVersion(self):
        '''
        usage: 程序更新方法
        '''
        versionUpgradePage = VersionUpgradePage(self.testcase, self.driver, self.logger)
        tempTimes = 0
        while versionUpgradePage.validSelf(False) and tempTimes < 3:
            versionUpgradePage.cancelVersionUpgrade()
            versionUpgradePage.waitBySeconds()
            tempTimes += 1

    def switchCity(self):
        '''
        usage: 选择城市方法
        '''
        switchCityPage = SwitchCityPage(self.testcase, self.driver, self.logger)
        tempTimes = 0
        while switchCityPage.validSelf(False) and tempTimes < 3:
            switchCityPage.cancelSwitchCity()
            switchCityPage.waitBySeconds()
            tempTimes += 1
    
    def backToDashBoard(self):
        '''
        usage: 返回主界面方法
        '''
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.clickLikeShopping()

    def closeHomeShakeTips(self):
        '''
        usage: 点击全城搜索方法
        '''
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.clickOnHomeShakeTips()

    def validLogoutStatus(self):
        '''
        usage: 验证退出登录方法
        '''
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.clickOnMy()
        myFfanPage = MyFfanPage(self.testcase, self.driver, self.logger)
        myFfanPage.validSelf()
        res = myFfanPage.isLoginStatus()
        if res:
            myFfanPage.clickOnSettings()
            settingPage = SettingsPage(self.testcase, self.driver, self.logger)
            settingPage.validSelf()
            settingPage.clickOnQuitAccountBtn()
            myFfanPage.waitBySeconds(seconds=2)
