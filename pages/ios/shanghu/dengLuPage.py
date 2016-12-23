# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text
from pages.logger import logger

class DengLuPage(SuperPage):

    def __init__(self, testcase, driver, logger):

        super(DengLuPage, self).__init__(testcase, driver, logger)



    def validSelf(self):
        logger.info('Check ' + Name.login + " begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  Name.login)
        logger.info('Check ' + Name.login + " end")
        API().screenShot(self.driver, "login")


    def inputUserName(self):
        '''
        输入用户名
        '''

        #获取焦点
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.username)
        #判断是否存在清除用户名按钮
        isClearUserButtonExist = API().validElementByXpath(self.driver, self.logger, Xpath.clearUserName)
        if isClearUserButtonExist:
            #点击清除用户名button
            API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.clearUserName)

        logger.info('Input ' +  Text.phoneNumber + ' begin')
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                               Xpath.username,
                               Text.phoneNumber)
        logger.info('Input ' + Text.phoneNumber + ' end')
        API().screenShot(self.driver, 'inputUsername')


    def inputPassword(self):
        '''
        输入密码
        :return:
        '''
        logger.info('Input ' + Text.password + ' begin')
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.password, Text.password)
        logger.info('Input ' + Text.password + ' end')
        API().screenShot(self.driver, 'inputPassword')



    def clickOnLoginButton(self):
        '''
        点击登录
        :return:
        '''
        logger.info("Click 登录 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.login)
        logger.info("Click 登录 end")
        API().screenShot(self.driver, 'clickLoginButton')


    def clickOnTestStoreItem(self):
        '''
        点击测试门店
        :return:
        '''
        logger.info("Click " + Name.test_store_name + ' begin')
        API().clickElementByName(self.testcase, self.driver, self.logger,Name.test_store_name)
        API().screenShot(self.driver, 'testStore')
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.button_select_store_submit)
        logger.info("Click " + Name.test_store_name + ' end')
        API().clickElementByName(self.testcase, self.driver, self.logger,Name.confirm_button)
        API().screenShot(self.driver, 'enterStore')


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
        logger.info("Click " + Name.settings + ' begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.settings)
        logger.info("Click " + Name.settings + ' end')
        API().screenShot(self.driver, 'setting')

    def clickOnLogout(self):
        '''
        点击退出登录
        :return:
        '''
        logger.info('Click 退出登录 begin')
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.logout)
        logger.info('Click 退出登录 end')
        API().screenShot(self.driver, 'logout')


    def validPassWord(self):
        '''
        验证密码框内容,如果为'请输入密码(长度8-20位)',则退出登录状态
        :return:
        '''
        logger.info('Check 密码框内容 begin')
        text_password = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.password)
        isLogoutStatus = (text_password == Text.initial_password)
        API().assertTrue(self.testcase,self.logger,isLogoutStatus)
        logger.info('Check 密码框内容 end')
        API().screenShot(self.driver, 'validLogout')
