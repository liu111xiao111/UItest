# -*- coding:utf-8 -*-

from selenium.common.exceptions import NoSuchElementException

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.cinema_page_configs import CinemaPageConfigs


class CinemaPage(SuperPage):
    '''
    作者 宋波
    首页=>电影=>电影详情=>电影院
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(CinemaPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_xpath_android(self.testcase, self.driver, self.logger,
                                           CinemaPageConfigs.xpath_cinema_title_st,
                                           CinemaPageConfigs.assert_view_timeout)

    def clickOnBuyTicket(self):
        '''
        usage: click on the buy ticket button.
        '''

        API().wait_by_seconds(20)
        self.scrollAsScreenPercent(0.5, 0.6, 0.5, 0.2)

        tempText = API().get_view_by_xpath_ios(self.driver, self.logger,
                                               CinemaPageConfigs.xpath_movie_name_st).text

        try:
            API().get_view_by_xpath_ios(self.driver, self.logger,
                                        CinemaPageConfigs.xpath_tomorrows_date_bt)
            API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                      CinemaPageConfigs.xpath_tomorrows_date_bt,
                                      CinemaPageConfigs.click_on_button_timeout)
        except NoSuchElementException:
            pass

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       CinemaPageConfigs.resource_id_buy_ticket_bt,
                                       CinemaPageConfigs.click_on_button_timeout)

        return tempText

if __name__ == '__main__':
    pass
