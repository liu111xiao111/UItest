# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text

class DengLuPage(SuperPage):

    def __init__(self, testcase, driver, logger):

        super(DengLuPage, self).__init__(testcase, driver, logger)



    def validSelf(self):
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  Name.login)


    def inputUserName(self):
        '''
        输入用户名
        '''

        #获取焦点
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.username)
        #点击清楚用户名button
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.clearUserName)


        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                               Xpath.username,
                               Text.phoneNumber)


    def inputPassword(self):
        '''
        输入密码
        :return:
        '''
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.password, Text.password)



    def clickOnLoginButton(self):
        '''
        点击登录
        :return:
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.login)


    def clickOnTestStoreItem(self):
        '''
        点击测试门店
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger,Name.test_store_name)
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.button_select_store_submit)


    def validLoginStatus(self):
        '''
        验证是否登录
        :return: false,true
        '''
        return API().validElementByName(self.driver,self.logger,Name.login,5)

    def clickOnSettings(self):
        '''
        点击设置
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.settings)

    def clickOnLogout(self):
        '''
        点击退出登录
        :return:
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.logout)


    def validPassWord(self):
        '''
        验证密码框内容,如果为'请输入密码(长度8-20位)',则退出登录状态
        :return:
        '''
        text_password = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.password)
        isLogoutStatus = (text_password == Text.initial_password)
        API().assertTrue(self.testcase,self.logger,isLogoutStatus)
