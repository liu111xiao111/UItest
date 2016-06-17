# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest

from appium import webdriver

from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.common.super_page import *
from com.qa.automation.appium.pages.android.ffan.dashboard_page_configs import *


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage :  进入应用的首页
'''
class DashboardPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(DashboardPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    '''
        usage : 进入到应用首页,检查ffan logo
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase=self.testcase , driver=self.driver, logger=self.logger ,
                                                resource_id=DashboardPageConfigs.resource_id__iv_logo__iv);

    def validSelfByText(self, text=DashboardPageConfigs.text_city_beijing):
        '''
            usage: verify whether the current page is valid by the text.
        '''

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger, text, DashboardPageConfigs.verify_view_timeout)

    '''
        usage： 点击我的个人信息
    '''
    def clickOnMy(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_mine);


    def clickOnSmartLife(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_huishenghuo);
        
    '''
       usage: 点击美食类目
    '''    
    def clickOnFood(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_food);
        
    '''
       usage: 点击亲子类目
    '''    
    def clickOnChildCategory(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_child);
    
    '''
       usage: 点击广场模块
    '''        
    def clickOnSquareModule(self):
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.logger, xpath=DashboardPageConfigs.xpath_square_module);    
    
    '''
        usage: 点击飞凡卡 
    '''       
    def clickOnFeiFanCard(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_feifan_card)
        
        
    '''
        usage: 点击返回dashboardpage
    '''    
    def clickLikeShopping(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_aiguangjie)
    
        
    def clickOnHomeShakeTips(self):
        '''
            usage: 点击摇一摇提示框
        '''
        API().click_view_by_resourceID_android(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = DashboardPageConfigs.resource_id_iv_home_shake_tips)

    
    def clickOnLefuCategory(self):
        '''
            usage: 点击"乐付"类目
        ''' 
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver,logger = self.logger,text = DashboardPageConfigs.text_lefu);

    def clickOnFlashSalesMore(self):
        '''
        usage: click flash sales more button
        '''

        tempWidth = API().get_width_of_device(self.driver, self.logger)
        tempHeight = API().get_height_of_device(self.driver, self.logger)
        API().scroll(self.driver, self.logger, tempWidth / 2, tempHeight * 2 / 3, tempWidth / 2, tempHeight / 3)
        API().scroll_to_text(self.driver, self.logger, DashboardPageConfigs.text_flash_sales_more_button)

    def clickOnParkingCategory(self):
        '''
            usage: 点击"停车"类目
        ''' 
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver,logger = self.logger,text = DashboardPageConfigs.text_parking);        API().click_view_by_resourceID_android(self.testcase, self.driver, self.logger, DashboardPageConfigs.resource_id_flash_sales_more_button, DashboardPageConfigs.click_on_button_timeout)


    def clickOnSearchView(self):
        '''
            usage:点击全城搜索
        '''     
        API().click_view_by_resourceID_android(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = DashboardPageConfigs.resource_id_tv_search_tv)
        
if __name__ == '__main__':
    pass;