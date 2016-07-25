# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API


class SuperPage(object):
    '''
    IOS SuperPage 方法
    '''
    def __init__(self, testcase, driver, logger):
        '''
        初始化函数
        '''
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def waitBySeconds(self, seconds=1):
        '''
        usage: 等待方法
        '''
        API().waitBySeconds(seconds)

    def clickBackKey(self):
        '''
        usage: 点击backkey方法
        '''
        API().clickBackKeyForIos(self.testcase, self.driver, self.logger,
                                 "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]")

    def screen_shot(self, screen_shot_name="myfeifan_auto_test"):
        '''
        usage: 截图方法
        '''
        API().screenShot(self.driver, screen_shot_name)

    def scrollAsScreenPercent(self, start_x_percent, start_y_percent, end_x_percent, end_y_percent, duration=800):
        '''
        usage: 百分比滑动界面方法
        '''
        x = API().getWidthOfDevice(self.driver, self.logger)
        y = API().getHeightOfDevice(self.driver, self.logger)
        
        API().scroll(self.driver, self.logger, x*start_x_percent,
                     y*start_y_percent, x*end_x_percent, y*end_y_percent,
                     duration)
        API().waitBySeconds(2)
