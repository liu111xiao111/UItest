# -*- coding: utf-8 -*-


from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.brand_category_page_configs import BrandCategoryPageConfigs


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
        usage : 判断
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=BrandCategoryPageConfigs.text_pinpaijie);

        

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

    def clickOnWomenFasion(self):
        '''
        usage : 点击 "女装" tab
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_women_fasion)

    def clickOnMenFasion(self):
        '''
        usage : 点击 "男装" tab
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_men_fasion)

    def clickOnCatering(self):
        '''
        usage : 点击 "餐饮" tab
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_catering)

    def clickOnLife(self):
        '''
        usage : 点击 "生活" tab
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_life)

    def clickOnSports(self):
        '''
        usage : 点击 "运动" tab
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_sports)

    def clickOnCompetitiveProducts(self):
        '''
        usage : 点击 "精品" tab
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_competitive_products)
    
    def clickOnDapairuzhu(self):
        '''
        usage : 点击 "精品" tab
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_dapairuzhu)

    def validSelfWomenFasion(self):
        '''
        usage : 判断 "女装" tab显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_women_fasion);

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
                                  
    def validDapairuzhu(self):
        '''
        usage : 判断 "精品" tab显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_dapai);

if __name__ == '__main__':
    pass;