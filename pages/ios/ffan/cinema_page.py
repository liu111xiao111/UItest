# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.cinema_page_configs import CinemaPageConfigs


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

        API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                   CinemaPageConfigs.xpath_cinema_title_st,
                                   CinemaPageConfigs.assert_view_timeout)

    def clickOnBuyTicket(self):
        '''
        usage: click on the buy ticket button.
        '''

        #API().waitBySeconds(20)
        #self.scrollAsScreenPercent(0.5, 0.6, 0.5, 0.2)

        tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                        CinemaPageConfigs.xpath_movie_name_st,
                                        CinemaPageConfigs.get_timeout)
        
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 CinemaPageConfigs.name_buy_ticket_bt,
                                 CinemaPageConfigs.click_on_button_timeout)
        '''
        if API().validElementByXpath(self.driver, self.logger, CinemaPageConfigs.xpath_tomorrows_date_bt,
                                     CinemaPageConfigs.valid_timeout):
            API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                      CinemaPageConfigs.xpath_tomorrows_date_bt,
                                      CinemaPageConfigs.click_on_button_timeout)

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 CinemaPageConfigs.resource_id_buy_ticket_bt,
                                 CinemaPageConfigs.click_on_button_timeout)
        '''
        return tempText


if __name__ == '__main__':
    pass
