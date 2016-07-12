# -*- coding:utf-8 -*-

import sys,os

import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner
from unittest.suite import TestSuite 
        
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.advertisement.hui_life_resource_niche_cases import HuiLifeResourceNicheCases
        
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.advertisement.\
        square_resource_niche_cases import SquareResourceNicheCases
        
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.cinema. \
         movie_ticket_cases import MovieTicketCases
         
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.cinema. \
         square_movie_cases import SquareMovieCases
         
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.coupon_and_activity.activity_sharing_cases import ActivitySharingCases
        
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.coupon_and_activity.privilege_coupon_cases import PrivilegeCouponCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.coupon_and_activity.sales_promotion_active_cases import SalesPromotionActiveCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.coupon_and_activity.sales_promotion_coupon_cases import SalesPromotionCouponCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.coupon_and_activity.special_offer_cases import SpecialOfferCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.coupon_and_activity.square_general_coupon_cases import SquareGeneralCouponCases


if __name__ == "__main__":
    build_num = sys.argv[1]
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/maguowei/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)
    
    suite = TestSuite()
    
#     suite.addTest(HuiLifeResourceNicheCases("test_case"))  ## didi pages not display.
#     suite.addTest(SquareResourceNicheCases("test_case"))
#     suite.addTest(MovieTicketCases("test_case"))
#     suite.addTest(SquareMovieCases("test_case"))
#     suite.addTest(ActivitySharingCases("test_case"))
#     suite.addTest(PrivilegeCouponCases("test_case"))  ###绑定“水云间满额赠礼活动”，强依赖特定数据
#     suite.addTest(SalesPromotionActiveCases("test_case"))
#     suite.addTest(SalesPromotionCouponCases("test_case"))
#     suite.addTest(SpecialOfferCases("test_case")) ### 慧生活没有活动和优惠tab了，delete case
    suite.addTest(SquareGeneralCouponCases("test_case"))
    
    
    now = time.strftime('%H_%M_%S')
    
    filename = reportpath + 'feifan_automation_test_report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
