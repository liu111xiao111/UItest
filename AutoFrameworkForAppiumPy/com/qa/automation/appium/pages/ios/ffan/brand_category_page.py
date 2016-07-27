# -*- coding: utf-8 -*-


from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.brand_category_page_configs import BrandCategoryPageConfigs


class BrandCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>品牌
    '''

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(BrandCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : 判断"推荐 & “大牌”显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=BrandCategoryPageConfigs.text_recommend);

        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=BrandCategoryPageConfigs.text_recommend);

    def clickOnBrand(self):
        '''
        usage : 点击 "大牌" tab
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = BrandCategoryPageConfigs.text_brand)

    def clickOnBrandDetails(self):
        '''
        usage : 点击进入大牌商品的详细页
        ''' 
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_brand_details); 

    def clickOnRecommendDetails(self):
        '''
        usage : 点击 "推荐" details
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_recommend_details)

    def clickOnMenFasion(self):
        '''
        usage : 点击 "男装" tab
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = BrandCategoryPageConfigs.text_men_fasion)

    def clickOnCatering(self):
        '''
        usage : 点击 "餐饮" tab
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = BrandCategoryPageConfigs.text_catering)

    def clickOnLife(self):
        '''
        usage : 点击 "生活" tab
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = BrandCategoryPageConfigs.text_life)

    def clickOnSports(self):
        '''
        usage : 点击 "运动" tab
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = BrandCategoryPageConfigs.text_sports)

    def clickOnCompetitiveProducts(self):
        '''
        usage : 点击 "精品" tab
        '''
        '''        print(API().get_width_of_device(self.driver, self.logger))
        print(API().get_height_of_device(self.driver, self.logger))
        start_x = API().get_width_of_device(self.driver, self.logger)/2
        end_x = API().get_width_of_device(self.driver, self.logger)/5
        start_y = API().get_height_of_device(self.driver, self.logger)/5
        end_y = API().get_height_of_device(self.driver, self.logger)/5'''
        '''API().scroll(self.driver,
                     self.logger,
                     190, 64, 150, 64)'''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = BrandCategoryPageConfigs.text_competitive_products)
        '''API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                       xpath = BrandCategoryPageConfigs.xpath_competitive_products)'''

    def validSelfMenFasion(self):
        '''
        usage : 判断 "男装" tab显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_men_fasion);

    def validSelfCertering(self):
        '''
        usage : 判断 "餐饮" tab显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_catering);

    def validSelfLife(self):
        '''
        usage : 判断 "生活" tab显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_life);

    def validSelfSports(self):
        '''
        usage : 判断 "运动" tab显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_sports);

    def validSelfCompetitiveProducts(self):
        '''
        usage : 判断 "精品" tab显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_competitive_products);


if __name__ == '__main__':
    pass;