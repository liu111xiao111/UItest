# -*- coding: utf-8 -*-

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from com.qa.automation.appium.pages.ffan.smart_life_page_configs import *
from com.qa.automation.appium.pages.common.super_page import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   慧生活page
class SmartLifePage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SmartLifePage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    '''
        usage : 进入慧生活,检查快车字段
    '''
    def validSelf(self):
        API().assert_view_by_text_android(testcase = self.testcase , driver = self.driver,logger = self.logger ,
                                                text = SmartLifePageConfigs.text_quickCar);

    '''
        usage : 进入慧生活,点击快车
    '''
    def clickQuickCar(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_quickCar);

    '''
        usage : 进入慧生活,点击出租车
    '''
    def clickTaxi(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_taxi);

    '''
        usage : 进入慧生活,点击专车
    '''
    def clickTailoredCar(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_tailoredCar);

    '''
        usage : 进入慧生活,点击代驾
    '''
    def clickDrivingService(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_drivingService);

    '''
        usage : 进入慧生活,点击挂号信息
    '''
    def clickRegister(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_register);

    '''
        usage : 进入慧生活,点击话费
    '''
    def clickTelephoneCharge(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_telephoneCharge);


    '''
        usage : 进入慧生活,点击流量
    '''
    def clickFlow(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_flow);


    '''
        usage : 进入慧生活,点击Q币
    '''
    def clickQCoin(self):
        API().click_view_by_text_android(driver=self.driver, logger=self.logger, text=SmartLifePageConfigs.text_qCoin);


    '''
        usage : 进入慧生活,点击游戏充值
    '''
    def clickGameCharge(self):
        API().click_view_by_text_android(driver=self.driver, logger=self.logger, text=SmartLifePageConfigs.text_gameCharge);


    '''
        usage : 进入慧生活,点击股票
    '''
    def clickStock(self):
        API().click_view_by_text_android(driver=self.driver, logger=self.logger, text=SmartLifePageConfigs.text_stock);


if __name__ == '__main__':
    pass;