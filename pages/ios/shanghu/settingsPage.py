from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.logger import logger
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text


class SettingsPage(SuperPage):

    def validSelf(self):
        '''
        验证设置页面
        '''
        logger.info('Check 设置页面 begin')
        API().assertElementByName(self.testcase, self.driver, self.logger, Name.settings)
        logger.info('Check 设置页面 end')
        API().screenShot(self.driver, 'settings')