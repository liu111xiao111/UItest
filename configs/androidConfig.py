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
    'WoDeLingHuaQianFeiTestCase'      : u'我的零花钱',
    'FeiFanTongFuKuanTestCase'        : u'飞凡通付款',
    'FeiFanTongKaGuanJiaTestCase'     : u'飞凡通卡管家',
    'FeiFanTongLingHuaQianTestCase'   : u'飞凡通零花钱',
    'HuiShengHuoTestCase'             : u'惠生活',
    'DianYingPiaoTestCase'            : u'电影',
    'GuangChangDianYingGuangTestCase' : u'广场电影逛',
    'GuangChangYouHuiQuanTestCase'    : u'广场优惠',
    'MeiShiHuiTestCase'               : u'美食汇',
    'GuangChangMeiShiHuiTestCase'     : u'广场美食汇',
    'GuangChangPaiDuiTestCase'        : u'广场排队取号',
    'PinPaiJieDaPaiTestCase'          : u'品牌街(大牌)',
    'PinPaiJieTuiJianTestCase'        : u'品牌街(推荐)',
    'GuangChangShiNeiDiTuTestCase'    : u'广场室内地图',
    'ShanPingShouYeTestCase'          : u'闪屏首页',
    'ChengShiQieHuanTestCase'         : u'城市切换',
    'WoDeTingCheJiaoFeiTestCase'      : u'我的停车缴费',
    'ShouYeTingCheTestCase'           : u'首页停车',
    'GuangChangTingCheTestCase'       : u'广场停车',
}