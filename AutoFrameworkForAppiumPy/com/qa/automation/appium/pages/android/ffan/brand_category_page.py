# -*- coding: utf-8 -*-


from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.brand_category_page_configs import BrandCategoryPageConfigs

#    推荐&大牌
class BrandCategoryPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(BrandCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : Load "推荐 & “大牌” page
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text = BrandCategoryPageConfigs.text_recommend, seconds=10);

    def clickOnBrand(self):
        '''
        usage : Click "大牌" tab
        '''
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text = BrandCategoryPageConfigs.text_brand)

    def clickOnBrandDetails(self):
        '''
        usage : Enter recommend details page
        ''' 
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = BrandCategoryPageConfigs.resource_id_tv_brand_details_tv); 

    def clickOnRecommendDetails(self):
        '''
        usage : Click "推荐" details
        '''
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = BrandCategoryPageConfigs.resource_id_tv_recommend_details_tv)

    def clickOnMenFasion(self):
        '''
        usage : Click "男装" tab
        '''
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text = BrandCategoryPageConfigs.text_men_fasion)

    def clickOnCatering(self):
        '''
        usage : Click "餐饮" tab
        '''
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text = BrandCategoryPageConfigs.text_catering)

    def clickOnLife(self):
        '''
        usage : Click "生活" tab
        '''
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text = BrandCategoryPageConfigs.text_life)

    def clickOnSports(self):
        '''
        usage : Click "运动" tab
        '''
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text = BrandCategoryPageConfigs.text_sports)

    def clickOnCompetitiveProducts(self):
        '''
        usage : Click "精品" tab
        '''
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text = BrandCategoryPageConfigs.text_competitive_products)

    def validSelfMenFasion(self):
        '''
        usage : Load "男装" tab
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text = BrandCategoryPageConfigs.text_men_fasion, seconds=10);

    def validSelfCertering(self):
        '''
        usage : Load "餐饮" tab
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text = BrandCategoryPageConfigs.text_catering, seconds=10);

    def validSelfLife(self):
        '''
        usage : Load "生活" tab
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text = BrandCategoryPageConfigs.text_life, seconds=10);

    def validSelfSports(self):
        '''
        usage : Load "运动" tab
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text = BrandCategoryPageConfigs.text_sports, seconds=10);

    def validSelfCompetitiveProducts(self):
        '''
        usage : Load "精品" tab
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text = BrandCategoryPageConfigs.text_competitive_products, seconds=10);

if __name__ == '__main__':
    pass;