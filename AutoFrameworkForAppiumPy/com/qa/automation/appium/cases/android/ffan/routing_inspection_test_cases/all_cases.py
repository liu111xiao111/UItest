# -*- coding:utf-8 -*-

import sys,os

import time
import traceback
import threading
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner
from unittest.suite import TestSuite
from com.qa.automation.appium.utility.mailProcess import sendTestResultMail
        
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

#from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.goods.brand_recommend_category_cases import BrandRecommendCatergoryCases

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

from com.qa.automation.appium.cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.common.performance import Performance
from com.qa.automation.appium.cases.android.ffan.common.reportProcess import ReportHandle
from com.qa.automation.appium.cases.android.ffan.common.performanceProcess import PerformanceHandle
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.fps_performance_test_cases import FpsPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.personal_information.login_cases import LoginCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.search.dashboard_search_goods_cases import DashboardSearchGoodsCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.search.dashboard_search_store_cases import DashboardSearchStoreCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.search.hot_word_search_cases import HotWordSearchCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.search.square_find_store_search_cases import SquareFindStoreSearchCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.search.square_search_cases import SquareSearchCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.child_category_cases import ChildCatergoryCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.lefu_cancel_category_cases import LefuCancelCatergoryCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.lefu_pay_category_cases import LefuPayCatergoryCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.shopping_category_cases import ShoppingCatergoryCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.shopping_mall_cases import ShoppingMallCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.square_lefu_pay_cases import SquareLefuPayCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.square_shopping_cases import SquareShoppingCases
from com.qa.automation.appium.cases.android.ffan.routing_inspection_test_cases.shopping.dashboard_square_cases import DashboardSquareCases

def runPerformance(reportPath):
    perf = Performance(reportPath)
    while True:
        perf.getCpu()
        perf.getMemory()
        perf.getTx()
        perf.getRx()

if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]

    #root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()

    suite.addTest(ShoppingMallCases("testCase"))
    suite.addTest(ChildCatergoryCases("test_case"))
    suite.addTest(DashboardSquareCases("test_case"))
    suite.addTest(MyfeifanMyTicketCases("test_case"))
    # suite.addTest(HuiLifeResourceNicheCases("testHuiLifeScreenShot"))
    # suite.addTest(SquareResourceNicheCases("test_case"))
    suite.addTest(MovieTicketCases("test_case"))
    suite.addTest(SquareMovieCases("test_case"))
    # suite.addTest(ActivitySharingCases("test_case")) # 首页优惠活动相关
    suite.addTest(PrivilegeCouponCases("test_case"))
    # suite.addTest(SalesPromotionActiveCases("test_case")) # 首页优惠活动相关
    # suite.addTest(SalesPromotionCouponCases("test_case")) # 首页优惠活动相关

    # suite.addTest(SpecialOfferCases("test_case")) # 慧生活没有活动和优惠tab了

    # suite.addTest(SquareGeneralCouponCases("test_case")) # 通用券相关
    # suite.addTest(SquareRecommendCases("test_case"))   # 达人推荐功能移除
    suite.addTest(FoodCases("test_case"))
    suite.addTest(SquareFoodCases("test_case"))
    suite.addTest(SquareQueueCases("test_case"))
    suite.addTest(BrandFamousCatergoryCases("test_case"))
    #suite.addTest(BrandRecommendCatergoryCases("test_case"))
    suite.addTest(SquareIndoorMapCases("test_case"))
    suite.addTest(SplashScreenHomePageCases("test_case"))
    suite.addTest(SwitchCityCases("test_case_step_2"))
    suite.addTest(MyfeifanMyParkingPaymentCases("test_case"))
    suite.addTest(ParkingBindingsCatergoryCases("test_case"))
    #suite.addTest(ParkingBundingCatergoryCases("test_case"))
    suite.addTest(SquareParkingPaymentCases("test_case"))
    suite.addTest(FeiFanCardBillCases("test_case"))
    suite.addTest(FeiFanCardIntegralCases("test_case"))
    # suite.addTest(FeiFanCardOpenCases("test_case")) #新版本不再有这个入口，用例删除掉
    suite.addTest(LoginCases("test_case"))
    #suite.addTest(LogoutCases("test_case"))
    suite.addTest(MembershipCardPackageCases("test_case"))
    suite.addTest(MessageSettingsCases("test_case"))
    suite.addTest(MyfeifanMyLikeCases("test_case"))
    suite.addTest(MyfeifanMyQueueCases("test_case"))
    # suite.addTest(MyfeifanMyTicketCases("test_case")) # 首页优惠活动相关
    suite.addTest(OneCardCases("test_case"))
    suite.addTest(PersonalInformationCases("test_case"))
    suite.addTest(SmallAmountPasswordLessPaymentCases("test_case"))
    suite.addTest(SquareMemberCases("test_case"))
    suite.addTest(SquareSignOnCases("test_case"))
    suite.addTest(UpdateLoginPasswordCases("test_case"))
    suite.addTest(DashboardSearchBrandCases("test_case"))
    suite.addTest(DashboardSearchGoodsCases("test_case"))
    suite.addTest(DashboardSearchStoreCases("test_case"))
    suite.addTest(HotWordSearchCases("test_case"))
    suite.addTest(SquareFindStoreSearchCases("test_case"))
    suite.addTest(SquareSearchCases("test_case"))
    #suite.addTest(ChildCatergoryCases("test_case"))
    suite.addTest(LefuPayCatergoryCases("test_case"))
    suite.addTest(ShoppingCatergoryCases("test_case"))
    # suite.addTest(ShoppingMallCases("testCase"))
    suite.addTest(SquareLefuPayCases("test_case"))
    suite.addTest(SquareShoppingCases("test_case"))

    now = time.strftime('%H_%M_%S')

    filename = os.path.join(reportpath, 'feifan_automation_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')

    perfThread = threading.Thread(target=runPerformance, args=(reportpath,))
    perfThread.setDaemon(True)
    perfThread.start()
    perf = Performance(reportpath)
    startTraffic, sTime = perf.getTraffic()
    startTime = time.strftime('%Y/%m/%d %H:%M:%S')
    runner.run(suite)

    try:
        ColdBootTimePerformanceTestCases().getColdBootTime(reportpath)
        WarmBootTimePerformanceTestCases().getWarmBootTime(reportpath)
        FpsPerformanceTestCases().getFpsPerf(reportpath)
    except:
        raise traceback.format_exc()
    finally:
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTraffic(startTraffic, endTraffic, round(eTime-sTime))

        PerformanceHandle().Handle(startTime, endTime, reportpath)

    ReportHandle().handle(reportpath)

    if sentMail:
        sendTestResultMail(reportpath, 'android')