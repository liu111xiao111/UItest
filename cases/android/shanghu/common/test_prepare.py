# -*- coding: utf-8 -*-

from pages.android.shanghu.denglu_page import DengLuPage
from pages.android.shanghu.xuanzemendian_page import XuanZeMenDianPage
from pages.android.shanghu.shouye_page import ShouYePage


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

    def prepare(self):
        '''
        usage: 测试前准备方法，移除更新和选择城市弹出框，并且根据选择判断是否需要登录
        '''
        shouYePage = ShouYePage(self , self.driver , self.logger)
        login = shouYePage.validLogin()

        if not login:
            self.login()

    def login(self):
        '''
        usage: 登录方法
        '''
        dengLuPage = DengLuPage(self , self.driver , self.logger)
        dengLuPage.validSelf()

        dengLuPage.inputUserName()
        dengLuPage.inputPassWord()
        dengLuPage.clickOnLoginBtn()

        xuanZeMenDianPage = XuanZeMenDianPage(self , self.driver , self.logger)
        xuanZeMenDianPage.waitBySeconds(2)
        xuanZeMenDianPage.validSelf()
        xuanZeMenDianPage.waitBySeconds(20)
        xuanZeMenDianPage.clickOnStore()
        xuanZeMenDianPage.clickOnConfirmBtn()
