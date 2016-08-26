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

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.coupon_and_activity.square_recommend_store_cases import SquareRecommendCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.foods.food_category_cases import FoodCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.foods.square_food_cases import SquareFoodCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.foods.square_queue_cases import SquareQueueCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.goods.brand_famous_category_cases import BrandFamousCatergoryCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.goods.brand_recommend_category_cases import BrandRecommendCatergoryCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.map.square_indoor_map_cases import SquareIndoorMapCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.others.splash_screen_home_page_cases import SplashScreenHomePageCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.others.switch_city_cases import SwitchCityCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.parking.myfeifan_my_parking_payment_cases import MyfeifanMyParkingPaymentCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.parking.parking_bindings_category_cases import ParkingBindingsCatergoryCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.parking.parking_bunding_category_cases import ParkingBundingCatergoryCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.parking.square_parking_payment_cases import SquareParkingPaymentCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.feifan_card_bill_cases import FeiFanCardBillCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.feifan_card_integral_cases import FeiFanCardIntegralCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.feifan_card_open_cases import FeiFanCardOpenCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.login_cases import LoginCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.logout_cases import LogoutCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.membership_card_package_cases import MembershipCardPackageCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.message_settings_cases import MessageSettingsCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.myfeifan_my_like_cases import MyfeifanMyLikeCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.myfeifan_my_queue_cases import MyfeifanMyQueueCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.myfeifan_my_ticket_cases import MyfeifanMyTicketCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.one_card_cases import OneCardCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.personal_information_cases import PersonalInformationCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.small_amount_password_less_payments_cases import SmallAmountPasswordLessPaymentCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.square_member_cases import SquareMemberCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.square_sign_on_cases import SquareSignOnCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.update_login_password_cases import UpdateLoginPasswordCases

from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.search.dashboard_search_brand_cases import DashboardSearchBrandCases

if __name__ == "__main__":
    build_num = sys.argv[1]

    #root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)
    
    suite = TestSuite()


    suite.addTest(HuiLifeResourceNicheCases("testHuiLifeScreenShot"))  ## didi pages not display.
    suite.addTest(SquareResourceNicheCases("test_case"))
    suite.addTest(MovieTicketCases("test_case"))
    suite.addTest(SquareMovieCases("test_case"))
    suite.addTest(ActivitySharingCases("test_case"))
    suite.addTest(PrivilegeCouponCases("test_case"))  ###绑定“水云间满额赠礼活动”，强依赖特定数据
    suite.addTest(SalesPromotionActiveCases("test_case"))
    suite.addTest(SalesPromotionCouponCases("test_case"))
    
#     suite.addTest(SpecialOfferCases("test_case")) ### 慧生活没有活动和优惠tab了，delete case

    suite.addTest(SquareGeneralCouponCases("test_case"))
    # suite.addTest(SquareRecommendCases("test_case"))   ## 达人推荐功能移除
    suite.addTest(FoodCases("test_case"))
    suite.addTest(SquareFoodCases("test_case"))
    suite.addTest(SquareQueueCases("test_case"))
    suite.addTest(BrandFamousCatergoryCases("test_case"))
    suite.addTest(BrandRecommendCatergoryCases("test_case"))
    suite.addTest(SquareIndoorMapCases("test_case"))
    suite.addTest(SplashScreenHomePageCases("test_case"))
    #suite.addTest(SwitchCityCases("test_case_prepare"))
    #suite.addTest(SwitchCityCases("test_case"))
    suite.addTest(MyfeifanMyParkingPaymentCases("test_case"))
    suite.addTest(ParkingBindingsCatergoryCases("test_case"))
    suite.addTest(ParkingBundingCatergoryCases("test_case"))
    suite.addTest(SquareParkingPaymentCases("test_case"))
    suite.addTest(FeiFanCardBillCases("test_case"))
    suite.addTest(FeiFanCardIntegralCases("test_case"))
    
#     suite.addTest(FeiFanCardOpenCases("test_case")) #新版本不再有这个入口，用例删除掉

    suite.addTest(LogoutCases("test_case"))
    suite.addTest(MembershipCardPackageCases("test_case"))
    suite.addTest(MessageSettingsCases("test_case"))
    suite.addTest(MyfeifanMyLikeCases("test_case"))
    suite.addTest(MyfeifanMyQueueCases("test_case"))
    suite.addTest(MyfeifanMyTicketCases("test_case"))
    suite.addTest(OneCardCases("test_case"))
    suite.addTest(PersonalInformationCases("test_case"))
    suite.addTest(SmallAmountPasswordLessPaymentCases("test_case"))
    suite.addTest(SquareMemberCases("test_case"))
    suite.addTest(SquareSignOnCases("test_case"))
    suite.addTest(UpdateLoginPasswordCases("test_case"))
    suite.addTest(DashboardSearchBrandCases("test_case"))
    
    now = time.strftime('%H_%M_%S')
    
    filename = reportpath + 'feifan_automation_test_report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
