# -*- coding: utf-8 -*-

from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil

appVersion = '4.8.0.0'

phoneVersion = 'iPhone5c'

buildVersion = '9.3.2'

deviceID = DeviceInfoUtil().getUdid()

caseList = {
    'BrandFamousCatergoryCases'             : u'品牌街',
    'ChildCatergoryCases'                   : u'亲子',
    'DashboardSearchBrandCases'             : u'全城搜索(品牌)',
    'DashboardSearchGoodsCases'             : u'全城搜索(商品)',
    'DashboardSearchStoreCases'             : u'全城搜索(门店)',
    'FeiFanCardBillCases'                   : u'飞凡通账单',
    'FeiFanCardIntegralCases'               : u'飞凡通其他快捷入口',
    'FeiFanCardOpenCases'                   : u'飞凡同市民/公交卡',
    'FoodCases'                             : u'美食汇',
    'HotWordSearchCases'                    : u'热词搜索',
    'LefuCancelCatergoryCases'              : u'买单',
    'LoginCases'                            : u'我的登录',
    'LogoutCases'                           : u'我的退出',
    'MembershipCardPackageCases'            : u'我的会员卡包',
    'MessageSettingsCases'                  : u'我的消息中心',
    'MovieTicketCases'                      : u'电影',
    'MyfeifanMyLikeCases'                   : u'我的喜欢',
    'OneCardCases'                          : u'我的飞凡通',
    'ParkingPaymentBindingsCases'           : u'首页停车',
    'ParkingPaymentCases'                   : u'我的停车缴费',
    'PersonalInformationCases'              : u'我的个人信息',
    'ShoppingMallCases'                     : u'购物中心',
    'SmallAmountPasswordLessPaymentCases'   : u'我的设置(小额免密设置)',
    'SquareFindStoreSearchCases'            : u'广场找店',
    'SquareFoodCases'                       : u'广场美食汇',
    'SquareLefuPayCases'                    : u'广场买单',
    'SquareParkingPaymentCases'             : u'广场停车',
    'SquareResourceNicheCases'              : u'广场资源位',
    'SquareSearchCases'                     : u'广场搜索',
    'SquareShoppingCases'                   : u'广场爱购物',
    'UpdateLoginPasswordCases'              : u'我的设置(修改密码)',
    'VersionUpgradeCases'                   : u'版本升级',
    'YaoyiyaoCases'                         : u'摇一摇',
    'SquareXianchangyaoCases'               : u'广场现场摇',
    'MyOrderCases'                          : u'我的订单',
    'SquareMembersCases'                    : u'广场会员',
    'MyfeifanMyQueueCases'                  : u'我的排队',
    'MyfeifanMyTicketCases'                 : u'我的票券',
    'SwitchCityCases'                       : u'城市切换',
    'SquareSignOnCases'                     : u'签到',
    'StoresAndSupermarketsCases'            : u'商超',
    'ShoppingCatergoryCases'                : u'名店优品',
    'SquareDetailsCases'                    : u'广场详情',
    'SquarePrivilegeCouponCases'            : u'广场优惠券',
    'SquareQueueCases'                      : u'广场排队取号',
    'SquareIndoorMapCases'                  : u'广场室内地图',
    'SquareMovieCases'                      : u'广场电影逛',
    'HuiLifeResourceNicheCases'             : u'慧生活入口',
    'SplashScreenHomePageCases'             : u"闪屏首页",
    'MyLinghuaqianCases'                    : u"我的零花钱",
    'MyFukuanmaCases'                       : u"我的付款码"
}
