# -*- coding: utf-8 -*-

from pages.android.ffan.switch_city_page import SwitchCityPage
from pages.android.ffan.version_upgrade_page import VersionUpgradePage
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.login_page import LoginPage
from pages.android.ffan.login_verify_page import LoginVerifyPage
from pages.android.ffan.settings_page import SettingsPage
from api.logger import logger


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
#         self.closeOlympicTip()
#         self.closeDoubleElevenTip()
        # self.updateVersion()
        self.closeLuckBugTip()
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
        logger.info("查看是否已经登录")
        if myFfanPage.isLoginStatus():
            logger.info("已经登录")
            return
        logger.info("未登录")
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(self.testcase, self.driver, self.logger)
        loginPage.validSelf()
        loginPage.switchToNormalLogin()
        loginPage.inputUserName()
        loginPage.inputPassWord()
        loginPage.waitBySeconds(3)
        loginPage.clickOnLoginBtn()
        myFfanPage.validSelf()
        dashboardPage.waitBySeconds(seconds=2)

#        if myFfanPage.validSelfOK() == True:

 ##          dashboardPage.waitBySeconds(seconds=2)
   #     else:
    #        loginPage.inputUserName()
     ##      loginPage.waitBySeconds(3)
       #     loginPage.clickOnLoginBtn()

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
        # 如果弹出切换城市Popup，点击取消按钮
        if switchCityPage.validSelf():
            switchCityPage.cancelSwitchCity()
        switchCityPage.waitBySeconds(2)
        # 验证当前城市为北京
        switchCityPage.validSelfCity()

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

    def closeOlympicTip(self):
        '''
        usage: 点击取消奥运抽奖
        '''
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.ClickOlympicCancleBtn()

    def closeDoubleElevenTip(self):
        '''
        usage: 点击取消双十一抽奖
        '''
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.ClickDoubleElevenCancleBtn()

    def closeLuckBugTip(self):
        '''
        usage: 点击取消圣诞抢福袋
        '''
        dashboardPage = DashboardPage(self.testcase, self.driver, self.logger)
        dashboardPage.ClickLuckBugCancleBtn()
