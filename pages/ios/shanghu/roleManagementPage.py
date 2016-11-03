# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text

class RoleManagementPage(SuperPage):

    def checkRoleList(self):
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_name)
        creator = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_creator)
        date = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_date)

        API().assertTrue(self.testcase, self.logger, not name is None)
        API().assertTrue(self.testcase, self.logger, not creator is None)
        API().assertTrue(self.testcase, self.logger, not date is None)
