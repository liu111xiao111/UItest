# -*- coding: utf-8 -*-

import sys, os

# reload(sys)
# sys.setdefaultencoding('utf8')

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.login_cases import LoginCases

import unittest

suite = unittest.TestLoader().loadTestsFromTestCase(LoginCases)
print("testcase number is %d" % (suite.countTestCases()));
rest = unittest.TextTestRunner(verbosity=2).run(suite);
print(type(rest))
print("error cases num %s" % (len(rest.errors)));
print(rest.failures);
