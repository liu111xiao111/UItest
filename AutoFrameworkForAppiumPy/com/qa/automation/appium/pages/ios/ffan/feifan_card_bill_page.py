# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.feifan_card_bill_page_configs import FeiFanCardBillPageConfigs


class FeiFanCardBillPage(SuperPage):
    '''
    作者 宋波
    首页=>飞凡卡=>飞凡卡账单
    '''

    def __init__(self, testcase, driver, logger):
        super(FeiFanCardBillPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查是否加载出来
    '''

    def validSelf(self):
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  FeiFanCardBillPageConfigs.resource_id_pocket_money_bill_st,
                                  FeiFanCardBillPageConfigs.assert_view_timeout)

    def validSubFilterByText(self, text=u"全部"):
        '''
        usage: verify whether the filter is correct.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger, text,
                                  FeiFanCardBillPageConfigs.click_on_button_timeout)

    def clickOnFilter(self):
        '''
        usage: click on the filter button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 FeiFanCardBillPageConfigs.resource_id_filter_bt,
                                 FeiFanCardBillPageConfigs.click_on_button_timeout)

    def clickOnSubFilterByText(self, text=u"全部"):
        '''
        usage: click on the sub-filter button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger, text,
                                 FeiFanCardBillPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass;
