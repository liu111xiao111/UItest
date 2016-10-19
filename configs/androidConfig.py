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




    'WoDeTingCheJiaoFeiTestCase'      : u'我的停车缴费',
    'ShouYeTingCheTestCase'           : u'首页停车',
    'GuangChangTingCheTestCase'       : u'广场停车',
    'WoDeLingHuaQianFeiTestCase'      : u'我的零花钱',
    'FeiFanTongFuKuanTestCase'        : u'飞凡通付款',
    'FeiFanTongKaGuanJiaTestCase'     : u'飞凡通卡管家',
    'FeiFanTongLingHuaQianTestCase'   : u'飞凡通零花钱',
    'HuiShengHuoTestCase'             : u'惠生活',
    'GuangChangDianYingGuangTestCase' : u'广场电影逛',
    'GuangChangYouHuiQuanTestCase'    : u'广场优惠',
    'GuangChangMeiShiHuiTestCase'     : u'广场美食汇',
    'GuangChangPaiDuiTestCase'        : u'广场排队取号',
    'GuangChangShiNeiDiTuTestCase'    : u'广场室内地图',
}