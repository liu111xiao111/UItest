#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from driver.android_driver import *
from pages.safari_activity import *

class LoginCases(AndroidDriver):

    def test_demo(self):
        safariActivity = SafariActivity(self.driver);
        safariActivity.clickOnTitleProfileIV();


if __name__ == "__main__":
    # print os.path.dirname(__file__);
    # print os.path.dirname(os.path.dirname(__file__));
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginCases)
    unittest.TextTestRunner(verbosity=2).run(suite)