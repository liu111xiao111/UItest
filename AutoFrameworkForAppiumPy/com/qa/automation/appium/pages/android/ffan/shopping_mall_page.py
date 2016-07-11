# -*- coding:utf-8 -*-

import operator

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.shopping_mall_page_configs import ShoppingMallPageConfigs

SMP = ShoppingMallPageConfigs()

class ShoppingMallPage(SuperPage):
    '''
    This is shopping mall page operation class.
    '''
    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''
        super(ShoppingMallPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SMP.resource_id_shopping_mall_title,
                                              SMP.assert_view_timeout)

    def clickOnTab(self, tab_number):
        '''
        usage: click on tab_list(total, mall, department) button.
        '''
        viewList = API().get_views_by_resourceID(self.driver,
                                                 self.logger,
                                                 SMP.resource_id_tab_id)
        viewList[tab_number-1].click()

    def validListView(self):
        '''
        usage: check ListView
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SMP.resource_id_plaza_id,
                                              SMP.assert_view_timeout)

    def validDistance(self):
        '''
        usage: check distance sequence
        '''

        elementList = API().get_views_text_contains_android(self.driver,
                                              self.logger,
                                              SMP.view_text_distance)
        
        plaza_number = len(elementList)
        if plaza_number > 1:
            for i in range(1, plaza_number):
                current_plaza_distance = elementList[i].text.split(" ")[0]
                prev_plaza_distance = elementList[i-1].text.split(" ")[0]
                if operator.gt(prev_plaza_distance, current_plaza_distance):
                    self.testcase.assertTrue(False, "The plaza distance is not ordered.")

    def clickOnBeijinTongzouMall(self):
        '''
        usage: click "北京通州万达广场"
        '''
        API().scroll_to_text(self.driver, self.logger, ShoppingMallPageConfigs.text_beijing_tongzou_mall)
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=ShoppingMallPageConfigs.text_beijing_tongzou_mall);


if __name__ == '__main__':
    pass
