# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.shangxueyuan_page_configs import ShangXueYuanPageConfigs as SXYPC
from pages.logger import logger


class ShangXueYuanPage(SuperPage):
    '''
    作者 乔佳溪
    商学院
    '''
    def __init__(self, testcase, driver, logger):
        super(ShangXueYuanPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到商学院页,检查登录标题
        '''
        logger.info("Check 商学院页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SXYPC.text_title,
                                  SXYPC.assert_timeout)
        logger.info("Check 商学院页面 end")

    def clickOnQuestion(self):
        '''
        usage: 点击常见问题
        '''
        logger.info("Click 常见问题 begin")
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SXYPC.text_question,
                                       SXYPC.assert_timeout)
        logger.info("Click 常见问题 end")

    def clickOnGuide(self):
        '''
        usage: 点击新手指南
        '''
        logger.info("Click 新手指南 begin")
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SXYPC.text_guide,
                                       SXYPC.assert_timeout)
        logger.info("Click 新手指南 end")

    def clickOnNotice(self):
        '''
        usage: 点击商家须知
        '''
        logger.info("Click 商家须知 begin")
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SXYPC.text_notice,
                                       SXYPC.assert_timeout)
        logger.info("Click 商家须知 end")

    def validQuestionDetails(self):
        '''
        usage : 验证常见问题
        '''
        logger.info("Check 常见问题 begin")
        title = []

        for i in range(5):
            xpath_problem = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[%s]/android.widget.TextView[1]" % (i+1)
            logger.info("Get 问题列表标题 begin")
            titleInfo = API().getTextByXpath(self.testcase,
                                             self.driver,
                                             self.logger,
                                             xpath_problem,
                                             SXYPC.assert_timeout)
            title.append(titleInfo)
            logger.info("Get 问题列表标题 end")

            logger.info("Click 进入第%s个问题 begin" % (i+1))
            API().clickElementByXpath(self.testcase,
                                      self.driver,
                                      self.logger,
                                      xpath_problem,
                                      SXYPC.assert_timeout)
            logger.info("Click 进入第%s个问题 end" % (i+1))

            logger.info("Check 第%s个问题标题 begin" % (i+1))
            API().getElementsByText(self.testcase,
                                      self.driver,
                                      self.logger,
                                      title[i],
                                      SXYPC.assert_timeout)
            logger.info("Check 第%s个问题标题 end" % (i+1))

            logger.info("Click 返回 begin")
            API().clickBackKeyForAndroid(self.driver, self.logger)
            logger.info("Click 返回 end")
        logger.info("Check 常见问题 end")

    def validGuideDetails(self):
        '''
        usage : 验证新手指南
        '''
        logger.info("Check 新手指南 begin")
        title = []

        for i in range(4):
            xpath_problem = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[%s]/android.widget.TextView[1]" % (i+1)

            titleInfo = API().getTextByXpath(self.testcase,
                                            self.driver,
                                            self.logger,
                                            xpath_problem,
                                            SXYPC.assert_timeout)
            title.append(titleInfo)

            API().clickElementByXpath(self.testcase,
                                      self.driver,
                                      self.logger,
                                      xpath_problem,
                                      SXYPC.assert_timeout)

            API().getElementsByText(self.testcase,
                                      self.driver,
                                      self.logger,
                                      title[i],
                                      SXYPC.assert_timeout)

            API().clickBackKeyForAndroid(self.driver, self.logger)
        logger.info("Check 新手指南 end")

    def validNoticeDetails(self):
        '''
        usage : 验证商家须知
        '''
        logger.info("Check 商家须知 begin")
        title = []

        for i in range(5):
            xpath_problem = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[%s]/android.widget.TextView[1]" % (i+1)

            titleInfo = API().getTextByXpath(self.testcase,
                                            self.driver,
                                            self.logger,
                                            xpath_problem,
                                            SXYPC.assert_timeout)

            title.append(titleInfo)

            API().clickElementByXpath(self.testcase,
                                      self.driver,
                                      self.logger,
                                      xpath_problem,
                                      SXYPC.assert_timeout)

            API().getElementsByText(self.testcase,
                                      self.driver,
                                      self.logger,
                                      title[i],
                                      SXYPC.assert_timeout)

            API().clickBackKeyForAndroid(self.driver, self.logger)
        logger.info("Check 商家须知 end")

