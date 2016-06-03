# -*- coding: utf-8 -*-

import sys,os
# reload(sys)
# sys.setdefaultencoding('utf8')

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.cases.ffan.myffan_cases import MyFfanCases
from com.qa.automation.appium.cases.ffan.love_shopping_cases import LoveShoppingCases
from com.qa.automation.appium.cases.ffan.smart_life_cases import SmartLifeCases

import unittest
import HTMLTestRunner
import time

build_num=sys.argv[1]

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))))
reportpath = "%s/report/ffan/%s/%s/" % (root_dir,time.strftime("%Y%m%d"),build_num)
# root_dir/ffan/date/build_num
if not os.path.exists(reportpath):
    os.makedirs(reportpath)


# suite = unittest.TestLoader().loadTestsFromTestCase(MyFfanCases)
suite = unittest.TestSuite()
suite.addTest(MyFfanCases("test_login"))
suite.addTest(MyFfanCases("test_logout"))

suite.addTest(LoveShoppingCases("test_shopping_mall"))
suite.addTest(LoveShoppingCases("test_film"))
suite.addTest(LoveShoppingCases("test_food"))
suite.addTest(LoveShoppingCases("test_brand"))
suite.addTest(LoveShoppingCases("test_children"))
suite.addTest(LoveShoppingCases("test_preferential"))
suite.addTest(LoveShoppingCases("test_shopping"))
suite.addTest(LoveShoppingCases("test_flash_sale"))
suite.addTest(LoveShoppingCases("test_parking"))
suite.addTest(LoveShoppingCases("test_le_pay"))

suite.addTest(SmartLifeCases("test_ClickQuickCar"))
suite.addTest(SmartLifeCases("test_clickTaxi"))
suite.addTest(SmartLifeCases("test_clickTailoredCar"))
suite.addTest(SmartLifeCases("test_clickDrivingService"))
# suite.addTest(SmartLifeCases("test_clickTelephoneCharge"))
# suite.addTest(SmartLifeCases("test_clickFlow"))
# suite.addTest(SmartLifeCases("test_clickQCoin"))
# suite.addTest(SmartLifeCases("test_clickGameCharge"))
# suite.addTest(SmartLifeCases("test_clickStock"))


filename = reportpath + 'feifan_automation_test_report.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                       description='Result for test')
runner.run(suite)