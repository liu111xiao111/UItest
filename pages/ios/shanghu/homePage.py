# -*- coding:utf-8 -*-


from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text

class HomePage(SuperPage):


   def __init__(self, testcase, driver, logger):

        super(HomePage, self).__init__(testcase, driver, logger)


   def validSelf(self):
       '''
        验证主页
       '''
       API.assertElementByName(self.testcase,self.driver,self.logger, Name.test_store_name)


   def clickOnPersonalInfo(self):
       '''
       点击右上角登录信息按钮
       :return:
       '''
       API().clickElementByXpath(self.testcase,self.driver,self.driver,Xpath.personalInfo)

   def validPersonalInfo(self):
        '''
        验证个人登录信息
        :return:
        '''
        API().assertElementByName(self.testcase, self.driver, self.logger, Name.userName)
        API().assertElementByName(self.testcase, self.driver, self.logger, Name.userIdentity)
        API().assertElementByName(self.testcase, self.driver, self.logger, Name.userStore)
        API().assertElementByName(self.testcase, self.driver, self.logger, Text.phoneNumber)