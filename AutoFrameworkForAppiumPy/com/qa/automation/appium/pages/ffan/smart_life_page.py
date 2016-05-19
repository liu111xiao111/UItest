# -*- coding: utf-8 -*-

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from com.qa.automation.appium.pages.ffan.smart_life_page_configs import *
from com.qa.automation.appium.pages.common.super_page import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   进入应用的首页,是进入其他页面的入口
class SmartLifePage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SmartLifePage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    '''
        usage : 进入慧生活,检查ffan logo
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase = self.testcase , driver = self.driver,logger = self.logger ,
                                                resource_id = SmartLifePageConfigs.resource_id__iv_logo__iv,seconds=18);

    '''
        usage : 进入慧生活,点击全城找店
    '''
    def clickFindStore(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_findStore);

    '''
        usage : 进入慧生活,点击排队
    '''
    def clickQueue(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_queue);

    '''
        usage : 进入慧生活,点击飞悦
    '''
    def clickFly(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_fly);

    '''
        usage : 进入慧生活,点击优惠券
    '''
    def clickCoupon(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_coupon);

    '''
        usage : 进入慧生活,点击活动
    '''
    def clickActivity(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.text_activity);

    '''
        usage : 进入慧生活,点击活动列表
    '''
    def clickActivityTag(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.tag_activity);


    '''
        usage : 进入慧生活,点击优惠列表
    '''
    def clickCouponTag(self):
        API().click_view_by_text_android(driver = self.driver,logger=self.logger,text=SmartLifePageConfigs.tag_coupon);


if __name__ == '__main__':
    pass;