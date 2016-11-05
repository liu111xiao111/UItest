# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.shangxueyuan_page_configs import ShangXueYuanPageConfigs as SXYPC


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
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SXYPC.text_title,
                                  SXYPC.assert_timeout)

    def clickOnQuestion(self):
        '''
        usage: 点击常见问题
        '''
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SXYPC.text_question,
                                       SXYPC.assert_timeout)

    def clickOnGuide(self):
        '''
        usage: 点击新手指南
        '''
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SXYPC.text_guide,
                                       SXYPC.assert_timeout)

    def clickOnNotice(self):
        '''
        usage: 点击商家须知
        '''
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SXYPC.text_notice,
                                       SXYPC.assert_timeout)

    def validQuestionDetails(self):
        '''
        usage : 验证常见问题
        '''
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

    def validGuideDetails(self):
        '''
        usage : 验证新手指南
        '''
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

    def validNoticeDetails(self):
        '''
        usage : 验证商家须知
        '''
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

