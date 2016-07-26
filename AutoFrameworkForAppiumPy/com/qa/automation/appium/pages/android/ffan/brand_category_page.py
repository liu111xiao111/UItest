# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.brand_category_page_configs import BrandCategoryPageConfigs as BCPC


class BrandCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>品牌
    '''
    def __init__(self,testcase,driver,logger):
        super(BrandCategoryPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证品牌页面
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  BCPC.text_recommend,
                                  BCPC.assert_view_timeout)

    def clickOnBrand(self):
        '''
        usage : 点击大牌
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 BCPC.text_brand,
                                 BCPC.click_view_timeout)

    def clickOnBrandDetails(self):
        '''
        usage : 点击品牌详情
        ''' 
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       BCPC.resource_id_tv_brand_details_tv,
                                       BCPC.click_view_timeout)

    def clickOnRecommendDetails(self):
        '''
        usage : 点击推荐详情
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       BCPC.resource_id_tv_recommend_details_tv,
                                       BCPC.click_view_timeout)

    def clickOnMenFasion(self):
        '''
        usage : 点击男装
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 BCPC.text_men_fasion,
                                 BCPC.click_view_timeout)

    def clickOnCatering(self):
        '''
        usage : 点击餐饮
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 BCPC.text_catering,
                                 BCPC.click_view_timeout)

    def clickOnLife(self):
        '''
        usage : 点击生活
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 BCPC.text_life,
                                 BCPC.click_view_timeout)

    def clickOnSports(self):
        '''
        usage : 点击运动
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 BCPC.text_sports,
                                 BCPC.click_view_timeout)

    def clickOnCompetitiveProducts(self):
        '''
        usage : 点击精品
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 BCPC.text_competitive_products,
                                 BCPC.click_view_timeout)

    def validSelfMenFasion(self):
        '''
        usage : 验证男装
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  BCPC.text_men_fasion,
                                  BCPC.assert_view_timeout)

    def validSelfCertering(self):
        '''
        usage : 验证餐饮
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  BCPC.text_catering,
                                  BCPC.assert_view_timeout)

    def validSelfLife(self):
        '''
        usage : 验证生活
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  BCPC.text_life,
                                  BCPC.assert_view_timeout)

    def validSelfSports(self):
        '''
        usage : 验证运动
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  BCPC.text_sports,
                                  BCPC.assert_view_timeout)

    def validSelfCompetitiveProducts(self):
        '''
        usage : 验证精品
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  BCPC.text_competitive_products,
                                  BCPC.assert_view_timeout)
