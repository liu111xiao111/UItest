# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.film_selector_page_configs import FilmSelectorPageConfigs


#   电影选择页面,入口:首页 -> 电影
class FilmSelectorPage(SuperPage):

    def __init__(self, test_case, driver, logger):
        super(FilmSelectorPage, self).__init__(testcase=test_case, driver=driver, logger=logger);

    """
        验证购物中心页面navigation bar name是否正确
    """
    def validSelf(self):
        navigation_bar = API().find_view_by_class_name_both(driver=self.driver,logger=self.logger,className=FilmSelectorPageConfigs.class_NavigationBar)
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           expect_text=FilmSelectorPageConfigs.name_film_selector_navigation_bar,
                           actual_text=navigation_bar.get_attribute("name"))

if __name__ == '__main__':
    pass;
