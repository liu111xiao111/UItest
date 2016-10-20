# -*- coding: utf-8 -*-

from utility.device_info_util import DeviceInfoUtil

appVersion = DeviceInfoUtil().getAppVersion()

phoneVersion = DeviceInfoUtil().getPhoneVersion()

buildVersion = DeviceInfoUtil().getBuildVersion()

deviceID = DeviceInfoUtil().getDeviceID()

caseList = {
    'ShanPingShouYeTestCase'          : u'闪屏首页',
    'ChengShiQieHuanTestCase'         : u'城市切换',
    'ReCiSouSuoTestCase'              : u'热词搜索',
    'DianYingTestCase'                : u'电影',
    'MeiShiHuiTestCase'               : u'美食汇',
    'PinPaiJieTestCase'               : u'品牌街',
    'QinZiTestCase'                   : u'亲子',
    'QianDaoTestCase'                 : u'签到',
    'ShangChaoTestCase'               : u'商超',
    'MingDianYouPinTestCase'          : u'名店优品',
    'ShouYeTingCheTestCase'           : u'首页停车',
    'MaiDanTestCase'                  : u'买单',
    'GuangChangXiangQingTestCase'     : u'广场详情',
    'GuangChangSouSuoTestCase'        : u'广场搜索',
    'GuangChangYouHuiQuanTestCase'    : u'广场优惠券',
    'GuangChangPaiDuiTestCase'        : u'广场排队取号',
    'GuangChangShiNeiDiTuTestCase'    : u'广场室内地图',
    'GuangChangTingCheTestCase'       : u'广场停车',
    'GuangChangDianYingGuangTestCase' : u'广场电影逛',
    'GuangChangMeiShiHuiTestCase'     : u'广场美食汇',
    'GuangChangAiGouWuTestCase'       : u'广场爱购物',
    'HuiShengHuoRuKouTestCase'        : u'惠生活入口',
    'HuiShengHuoJingXuanTestCase'     : u'惠生活精选/荐店',
    'WoDeDengLuTestCase'              : u'我的登录',
    'WoDeGeRenXinXiTestCase'          : u'我的个人信息',
    'WoDePiaoQuanTestCase'            : u'我的票券',
    'WoDeDingDanTestCase'             : u'我的订单',
    'WoDeHuiYuanKaBaoTestCase'        : u'我的会员卡包',
    'WoDeFeiFanTongTestCase'          : u'我的飞凡通',
    'WoDePaiDuiTestCase'              : u'我的排队',
    'WoDeTingCheJiaoFeiTestCase'      : u'我的停车缴费',
    'WoDeXiaoXiZhongXinTestCase'      : u'我的消息中心',
    'WoDeTuiChuTestCase'              : u'我的退出',




    'WoDeLingHuaQianFeiTestCase'      : u'我的零花钱',
    'FeiFanTongFuKuanTestCase'        : u'飞凡通付款',
    'FeiFanTongKaGuanJiaTestCase'     : u'飞凡通卡管家',
    'FeiFanTongLingHuaQianTestCase'   : u'飞凡通零花钱',
    'QuanChengSouSuoPinPaiTestCase'   : u'全城搜索(品牌)',
    'QuanChengSouSuoShangPinTestCase' : u'全城搜索(商品)',
    'QuanChengSouSuoMenDianTestCase'  : u'全城搜索(门店)',
    'GouWuZhongXinTestCase'           : u'购物中心',
    'GuangChangZhaoDianTestCase'      : u'广场找店',
    'GuangChangXianChangYaoTestCase'  : u'广场现场摇',
    'GuangChangMaiDanTestCase'        : u'广场买单',
    'GuangChangHuiYuanTestCase'       : u'广场会员',
    'GuangChangYouHuiTestCase'        : u'广场优惠',
    'FeiFanTongZhangDanTestCase'      : u'飞凡通账单',
    'FeiFanTongQiTaKuaiJieRuKouTestCase'        : u'飞凡通其他快捷入口',
    'YaoYiYaoTestCase'                          : u'摇一摇',
    'WoDeFuKuanMaTestCase'                      : u'我的付款码',
    'WoDeSheZhiXiuGaiDengLuMiMaTestCase'        : u'我的设置(修改登录密码)',
    'WoDeSheZhiXiuGaiZhiFuMiMaTestCase'         : u'我的设置(修改支付密码)',
    'WoDeSheZhiXiuGaiXiaoEMianMiZhiFuTestCase'  : u'我的设置(修改小额免密支付支付)',
}