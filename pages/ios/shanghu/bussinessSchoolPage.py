# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text
from pages.logger import logger

class BussinessSchoolPage(SuperPage):

    def back(self):
        '''
        返回动作
        :return:
        '''
        logger.info("Click back key, begin")
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.back_icon)
        logger.info("Click back key, end")

    def enterCommonQuestions(self):
        '''
        点击进入常见问题
        :return:
        '''
        logger.info("Click " + Name.bussiness_school_common_questions + ' begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.bussiness_school_common_questions)
        logger.info("Click " + Name.bussiness_school_common_questions + ' end')

    def checkCommonQuestionsItems(self):
        '''
        验证常见问题前5个,点击进入,检查内容
        :return:
        '''
        for count in range(5):
            commonText = API().getTextByXpath(self.testcase,
                                              self.driver,
                                              self.logger,
                                              "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]" % ( count + 1 ) + "/UIAStaticText[1]")

            API().clickElementByXpath(self.testcase,
                                    self.driver,
                                    self.logger,
                                    "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]" % (count + 1) + "/UIAStaticText[1]")
            logger.info('Check ' + commonText )
            #进入问题页面验证,问题文本
            API().assertElementByName(self.testcase, self.driver, self.logger,commonText)

            self.back()

    def enterNewerGuide(self):
        '''
        进入新手指南
        :return:
        '''
        logger.info("Click " +Name.bussiness_school_newer_guide + ' begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.bussiness_school_newer_guide)
        logger.info("Click " + Name.bussiness_school_newer_guide + ' end')

    def checkNewergudieItems(self):
        '''
        验证常见问题前4个,点击进入,检查内容
        :return:
        '''

        for count in range(4):
            commonText = API().getTextByXpath(self.testcase,
                                              self.driver,
                                              self.logger,
                                              "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]" % ( count + 1 ) + "/UIAStaticText[1]")

            API().clickElementByXpath(self.testcase,
                                    self.driver,
                                    self.logger,
                                    "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]" % (count + 1) + "/UIAStaticText[1]")
            logger.info('Check ' + commonText)
            #进入问题页面验证,问题文本
            API().assertElementByName(self.testcase, self.driver, self.logger,commonText)

            self.back()

    def enterSellerNotices(self):
        '''
        进入商家须知
        :return:
        '''
        logger.info("Click " + Name.bussiness_school_newer_guide + ' begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.bussiness_school_seller_notices)
        logger.info("Click " + Name.bussiness_school_newer_guide + ' end')

    def checkSellerNoticesItems(self):
        '''
        验证常见问题前5个,点击进入,检查内容
        :return:
        '''

        for count in range(4):
            commonText = API().getTextByXpath(self.testcase,
                                              self.driver,
                                              self.logger,
                                              "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]" % ( count + 1 ) + "/UIAStaticText[1]")

            API().clickElementByXpath(self.testcase,
                                    self.driver,
                                    self.logger,
                                    "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]" % (count + 1) + "/UIAStaticText[1]")
            API().assertElementByName(self.testcase, self.driver, self.logger, commonText)
            #进入问题页面验证,问题文本
            API().assertElementByName(self.testcase, self.driver, self.logger,commonText)

            self.back()