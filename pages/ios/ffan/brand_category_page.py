# -*- coding: utf-8 -*-


from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.brand_category_page_configs import BrandCategoryPageConfigs
from pages.logger import logger

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
        logger.info("Check 品牌 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=BrandCategoryPageConfigs.text_pinpaijie);
        API().screenShot(self.driver,"pinPai")
        logger.info("Check 品牌 end")
        

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
        logger.info("Click 女装 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_women_fasion)
        logger.info("Click 女装 end")

    def clickOnMenFasion(self):
        '''
        usage : 点击 "男装" tab
        '''
        logger.info("Click 男装 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_men_fasion)
        logger.info("Click 男装 end")

    def clickOnCatering(self):
        '''
        usage : 点击 "餐饮" tab
        '''
        logger.info("Click 餐饮 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_catering)
        logger.info("Click 餐饮 end")

    def clickOnLife(self):
        '''
        usage : 点击 "生活" tab
        '''
        logger.info("Click 生活 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_life)
        logger.info("Click 生活 end")

    def clickOnSports(self):
        '''
        usage : 点击 "运动" tab
        '''
        logger.info("Click 运动 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_sports)
        logger.info("Click 运动 end")

    def clickOnCompetitiveProducts(self):
        '''
        usage : 点击 "精品" tab
        '''
        logger.info("Click 精品 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = BrandCategoryPageConfigs.xpath_competitive_products)
        logger.info("Click 精品 end")
    
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
        logger.info("Check 女装 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_women_fasion);
        logger.info("Check 女装 end")
        API().screenShot(self.driver, "nvZhuang")

    def validSelfMenFasion(self):
        '''
        usage : 判断 "男装" tab显示是否正确
        '''
        logger.info("Check 男装 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_men_fasion);
        logger.info("Check 男装 end")
        API().screenShot(self.driver, "nanZhuang")

    def validSelfCertering(self):
        '''
        usage : 判断 "餐饮" tab显示是否正确
        '''
        logger.info("Check 餐饮 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_catering);
        logger.info("Check 餐饮 end")
        API().screenShot(self.driver,"nanZhuang")

    def validSelfLife(self):
        '''
        usage : 判断 "生活" tab显示是否正确
        '''
        logger.info("Check 生活 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_life);
        logger.info("Check 生活 end")
        API().screenShot(self.driver, "shengHuo")

    def validSelfSports(self):
        '''
        usage : 判断 "运动" tab显示是否正确
        '''
        logger.info("Check 运动 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_sports);
        logger.info("Check 运动 end")
        API().screenShot(self.driver, "yunDong")

    def validSelfCompetitiveProducts(self):
        '''
        usage : 判断 "精品" tab显示是否正确
        '''
        logger.info("Check 精品 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_competitive_products);
        logger.info("Check 精品 end")
        API().screenShot(self.driver, "jingPin")



    def validDapairuzhu(self):
        '''
        usage : 判断 "精品" tab显示是否正确
        '''
        logger.info("Check 大牌精品 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name = BrandCategoryPageConfigs.text_dapai);
        logger.info("Check 大牌精品 end")
        API().screenShot(self.driver, "daPaiJingPin")

if __name__ == '__main__':
    pass;