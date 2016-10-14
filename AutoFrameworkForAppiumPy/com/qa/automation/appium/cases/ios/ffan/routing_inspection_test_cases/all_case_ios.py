# -*- coding:utf-8 -*-

import sys,os

import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner
from unittest.suite import TestSuite

from com.qa.automation.appium.cases.ios.ffan.common.reportProcess import ReportHandle
from com.qa.automation.appium.utility.mailProcess import sendTestResultMail

from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.activity_sharing_cases import ActivitySharingCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.brand_famous_category_cases import BrandFamousCatergoryCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.brand_recommend_category_cases import BrandRecommendCatergoryCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.child_category_cases import ChildCatergoryCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.dashboard_search_brand_cases import DashboardSearchBrandCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.dashboard_search_goods_cases import DashboardSearchGoodsCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.dashboard_search_store_cases import DashboardSearchStoreCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.feifan_card_bill_cases import FeiFanCardBillCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.feifan_card_integral_cases import FeiFanCardIntegralCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.feifan_card_open_cases import FeiFanCardOpenCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.food_category_cases import FoodCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.hot_word_search_cases import HotWordSearchCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.hui_life_resource_niche_cases import HuiLifeResourceNicheCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.lefu_cancel_category_cases import LefuCancelCatergoryCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.lefu_pay_category_cases import LefuPayCatergoryCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.login_cases import LoginCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.logout_cases import LogoutCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.membership_card_package_cases import MembershipCardPackageCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.message_settings_cases import MessageSettingsCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.movie_ticket_cases import MovieTicketCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.myfeifan_my_like_cases import MyfeifanMyLikeCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.myfeifan_my_queue_cases import MyfeifanMyQueueCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.myfeifan_my_ticket_cases import MyfeifanMyTicketCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.one_card_cases import OneCardCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.parking_payment_bindings_cases import ParkingPaymentBindingsCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.parking_payment_cases import ParkingPaymentCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.parking_payment_unbinding_cases import ParkingPaymentUnbindingCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.personal_information_cases import PersonalInformationCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.privilege_coupon_cases import PrivilegeCouponCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.sales_promotion_active_cases import SalesPromotionActiveCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.sales_promotion_coupon_cases import SalesPromotionCouponCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.shopping_category_cases import ShoppingCatergoryCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.shopping_mall_cases import ShoppingMallCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.small_amount_password_less_payments_cases import SmallAmountPasswordLessPaymentCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.special_offer_cases import SpecialOfferCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.splash_screen_home_page_cases import SplashScreenHomePageCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_find_store_search_cases import SquareFindStoreSearchCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_food_cases import SquareFoodCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_general_coupon_cases import SquareGeneralCouponCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_indoor_map_cases import SquareIndoorMapCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_lefu_pay_cases import SquareLefuPayCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_movie_cases import SquareMovieCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_parking_payment_cases import SquareParkingPaymentCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_queue_cases import SquareQueueCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_recommend_store_cases import SquareRecommendCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_resource_niche_cases import SquareResourceNicheCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_search_cases import SquareSearchCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_shopping_cases import SquareShoppingCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_sign_on_cases import SquareSignOnCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.switch_city_cases import SwitchCityCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.update_login_password_cases import UpdateLoginPasswordCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.version_upgrade_cases import VersionUpgradeCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.yao_yi_yao_cases import YaoyiyaoCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_xianchangyao_cases import SquareXianchangyaoCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.my_order_cases import MyOrderCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.square_members_cases import SquareMembersCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.myfeifan_my_queue_cases import MyfeifanMyQueueCases
from com.qa.automation.appium.cases.ios.ffan.routing_inspection_test_cases.myfeifan_my_ticket_cases import MyfeifanMyTicketCases


if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]


    #root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    #reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/auto/workspace_pycharm/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()
    
    # suite.addTest(ActivitySharingCases("test_case"))
    suite.addTest(BrandFamousCatergoryCases("test_case"))
    #suite.addTest(BrandRecommendCatergoryCases("test_case"))

    suite.addTest(ChildCatergoryCases("test_case"))
    
    suite.addTest(DashboardSearchBrandCases("test_case"))
    
    suite.addTest(DashboardSearchGoodsCases("test_case"))
    suite.addTest(DashboardSearchStoreCases("test_case"))
    suite.addTest(FeiFanCardBillCases("test_case"))
    suite.addTest(FeiFanCardIntegralCases("test_case"))
    suite.addTest(FeiFanCardOpenCases("test_case"))
    suite.addTest(FoodCases("test_case"))
    suite.addTest(HotWordSearchCases("test_case"))
    #suite.addTest(HuiLifeResourceNicheCases("test_case"))
    suite.addTest(LefuCancelCatergoryCases("test_case"))
    suite.addTest(LoginCases("test_case"))
    suite.addTest(LogoutCases("test_case"))
    suite.addTest(MembershipCardPackageCases("test_case"))
    suite.addTest(MessageSettingsCases("test_case"))
    suite.addTest(MovieTicketCases("test_case"))
    suite.addTest(MyfeifanMyLikeCases("test_case"))
    #suite.addTest(MyfeifanMyQueueCases("test_case"))
    #suite.addTest(MyfeifanMyTicketCases("test_case"))
    suite.addTest(OneCardCases("test_case"))
    suite.addTest(ParkingPaymentBindingsCases("test_case"))
    suite.addTest(ParkingPaymentCases("test_case"))
    #suite.addTest(ParkingPaymentUnbindingCases("test_case"))
    suite.addTest(PersonalInformationCases("test_case"))
    #suite.addTest(PrivilegeCouponCases("test_case"))
    #suite.addTest(SalesPromotionActiveCases("test_case"))
    #suite.addTest(SalesPromotionCouponCases("test_case"))
    #suite.addTest(ShoppingCatergoryCases("test_case"))
    suite.addTest(ShoppingMallCases("testCase"))
    suite.addTest(SmallAmountPasswordLessPaymentCases("test_case"))
    #suite.addTest(SpecialOfferCases("test_case"))
    #suite.addTest(SplashScreenHomePageCases("test_case"))
    suite.addTest(SquareFindStoreSearchCases("test_case"))
    suite.addTest(SquareFoodCases("test_case"))
    #suite.addTest(SquareGeneralCouponCases("test_case"))
    #suite.addTest(SquareIndoorMapCases("test_case"))
    suite.addTest(SquareLefuPayCases("test_case"))
    #suite.addTest(SquareMovieCases("test_case"))
    suite.addTest(SquareParkingPaymentCases("test_case"))
    #suite.addTest(SquareLefuPayCases("test_case"))
    #suite.addTest(SquareRecommendCases("test_case"))
    suite.addTest(SquareResourceNicheCases("test_case"))
    suite.addTest(SquareSearchCases("test_case"))
    suite.addTest(SquareShoppingCases("test_case"))
    #suite.addTest(SquareSignOnCases("test_case"))
    suite.addTest(UpdateLoginPasswordCases("test_case"))
    suite.addTest(VersionUpgradeCases("test_case"))
    suite.addTest(YaoyiyaoCases("test_case"))
    suite.addTest(SquareXianchangyaoCases("test_case"))
    suite.addTest(MyOrderCases("test_case"))
    #suite.addTest(LefuPayCatergoryCases("test_case"))
    suite.addTest(SquareMembersCases("test_case"))
    suite.addTest(MyfeifanMyQueueCases("test_case"))
    suite.addTest(MyfeifanMyTicketCases("test_case"))

    suite.addTest(SwitchCityCases("test_case"))
    



    now = time.strftime('%H_%M_%S')

    filename = reportpath + 'feifan_automation_test_report_ios.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report_ios',
                                           description='Result for test')
    runner.run(suite)

    ReportHandle().handle(reportpath)

    if sentMail:
        sendTestResultMail(reportpath, 'ios')
