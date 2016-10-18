# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

def getAppVersion():
    version = ''
    versionCmd = 'adb shell dumpsys package com.wanda.app.wanhui | grep versionName'
    ret = Popen(versionCmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = ret.communicate()
    if out:
        version = out.decode('utf-8').split('=')[1].split('\r\n')[0]

    return version

appVersion = getAppVersion()

def getPhoneVersion():
    brand = ''
    mode = ''
    brandCmd = 'adb shell cat /system/build.prop | grep "product.brand"'
    modeCmd = 'adb shell cat /system/build.prop | grep "product.mode"'
    ret = Popen(brandCmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = ret.communicate()
    if out:
        brand = out.decode('utf-8').split('=')[1].split('\r\n')[0]
    ret = Popen(modeCmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = ret.communicate()
    if out:
        mode = out.decode('utf-8').split('=')[1].split('\r\n')[0]

    return brand.upper() + ' ' + mode.upper()

phoneVersion = getPhoneVersion()

caseList = {
    'MyfeifanMyBillCases'                   : u'我的零花钱',
    'FeiFanCardPaymentCases'                : u'飞凡通付款',
    'FeiFanCardManagerCases'                : u'飞凡通卡管家',
    'FeiFanCardChargeCases'                 : u'飞凡通零花钱',
    'ShoppingMallCases'                     : u'购物中心',
    'ChildCatergoryCases'                   : u'亲子',
    'DashboardSquareCases'                  : u'广场详情',
    'MyfeifanMyTicketCases'                 : u'我的票券',
    'MyfeifanMyOrderCases'                  : u'我的订单',
    'HuiLifeEntranceCases'                  : u'慧生活入口',
    'HuiLifeSelectShopCases'                : u'慧生活精选/荐店',
    'SquareSalesCases'                      : u'广场优惠',
    'DashboardShakeCases'                   : u'摇一摇',
    'SquareShakeCases'                      : u'广场现场摇',
    'MyfeifanMyPaymentCodeCases'            : u'我的付款码',
    'MovieTicketCases'                      : u'电影',
    'SquareMovieCases'                      : u'广场电影逛',
    'PrivilegeCouponCases'                  : u'广场优惠券',
    'FoodCases'                             : u'美食汇',
    'SquareFoodCases'                       : u'广场美食汇',
    'SquareQueueCases'                      : u'广场排队取号',
    'BrandFamousCatergoryCases'             : u'品牌街',
    'SquareIndoorMapCases'                  : u'广场室内地图',
    'SplashScreenHomePageCases'             : u'闪屏首页',
    'SwitchCityCases'                       : u'城市切换',
    'MyfeifanMyParkingPaymentCases'         : u'我的停车缴费',
    'ParkingBindingsCatergoryCases'         : u'首页停车',
    'SquareParkingPaymentCases'             : u'广场停车',
    'FeiFanCardBillCases'                   : u'飞凡通账单',
    'FeiFanCardIntegralCases'               : u'飞凡通其他快捷入口',
    'LoginCases'                            : u'我的登录',
    'MembershipCardPackageCases'            : u'我的会员卡包',
    'MessageSettingsCases'                  : u'我的消息中心',
    'MyfeifanMyLikeCases'                   : u'我的喜欢',
    'MyfeifanMyQueueCases'                  : u'我的排队',
    'OneCardCases'                          : u'我的飞凡通',
    'PersonalInformationCases'              : u'我的个人信息',
    'PaymentPasswordSettingCases'           : u'我的设置(修改支付密码)',
    'SmallAmountPasswordLessPaymentCases'   : u'我的设置(小额免密设置)',
    'SquareMemberCases'                     : u'广场会员',
    'SquareSignOnCases'                     : u'签到',
    'UpdateLoginPasswordCases'              : u'我的设置(修改登录密码)',
    'DashboardSearchBrandCases'             : u'全城搜索(品牌)',
    'DashboardSearchGoodsCases'             : u'全城搜索(商品)',
    'DashboardSearchStoreCases'             : u'全城搜索(门店)',
    'HotWordSearchCases'                    : u'热词搜索',
    'SquareFindStoreSearchCases'            : u'广场找店',
    'SquareSearchCases'                     : u'广场搜索',
    'LefuPayCatergoryCases'                 : u'买单',
    'ShoppingCatergoryCases'                : u'名店优品',
    'SquareLefuPayCases'                    : u'广场买单',
    'SquareShoppingCases'                   : u'广场爱购物',
    'DashboardSupermarketCases'             : u'商超',
}
