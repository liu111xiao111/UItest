# -*- coding: utf-8 -*-

from pages.ios.shanghu.dengLuPage import DengLuPage
from pages.ios.shanghu.homePage import HomePage


class Prepare:

    def __init__(self, testcase, driver, logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def login(self):
        dengLuPage = DengLuPage(self, self.driver, self.logger)
        homePage = HomePage(self, self.driver, self.logger)

        # 检查是否登录,如果已经登录,点击退出登录
        loginStatus = dengLuPage.validLoginStatus()
        # self.logger.i(loginStatus)
        if not loginStatus:
            pass
        else:
            dengLuPage.validSelf()
            dengLuPage.inputUserName()
            dengLuPage.inputPassword()
            dengLuPage.clickOnLoginButton()

            dengLuPage.clickOnTestStoreItem()

