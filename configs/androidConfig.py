# -*- coding: utf-8 -*-

from utility.device_info_util import DeviceInfoUtil

appVersion = DeviceInfoUtil().getAppVersion()

phoneVersion = DeviceInfoUtil().getPhoneVersion()

buildVersion = DeviceInfoUtil().getBuildVersion()

deviceID = DeviceInfoUtil().getDeviceID()

caseList = {
    'ShanPingShouYeTestCase'                    : [u'闪屏首页', '1'],
    'ChengShiQieHuanTestCase'                   : [u'城市切换', '2'],
    'QuanChengSouSuoPinPaiTestCase'             : [u'全城搜索(品牌)', '3-1'],
    'QuanChengSouSuoShangPinTestCase'           : [u'全城搜索(商品)', '3-2'],
    'QuanChengSouSuoMenDianTestCase'            : [u'全城搜索(门店)', '3-3'],
    'ReCiSouSuoTestCase'                        : [u'热词搜索', '4'],
    'GouWuZhongXinTestCase'                     : [u'购物中心', '5'],
    'DianYingTestCase'                          : [u'电影', '6'],
    'MeiShiHuiTestCase'                         : [u'美食汇', '7'],
    'PinPaiJieTestCase'                         : [u'品牌街', '8'],
    'QinZiTestCase'                             : [u'亲子', '9'],
    'QianDaoTestCase'                           : [u'签到', '10'],
    'ShangChaoTestCase'                         : [u'商超', '11'],
    'MingDianYouPinTestCase'                    : [u'名店优品', '14'],
    'ShouYeTingCheTestCase'                     : [u'首页停车', '16'],
    'MaiDanTestCase'                            : [u'买单', '17'],
    'GuangChangXiangQingTestCase'               : [u'广场详情', '21'],
    'GuangChangSouSuoTestCase'                  : [u'广场搜索', '22'],
    'GuangChangZhaoDianTestCase'                : [u'广场找店', '24'],
    'GuangChangYouHuiQuanTestCase'              : [u'广场优惠券', '25'],
    'GuangChangXianChangYaoTestCase'            : [u'广场现场摇', '26'],
    'GuangChangPaiDuiTestCase'                  : [u'广场排队取号', '27'],
    'GuangChangShiNeiDiTuTestCase'              : [u'广场室内地图', '28'],
    'GuangChangTingCheTestCase'                 : [u'广场停车', '29'],
    'GuangChangMaiDanTestCase'                  : [u'广场买单', '30'],
    'GuangChangHuiYuanTestCase'                 : [u'广场会员', '31'],
    'GuangChangDianYingGuangTestCase'           : [u'广场电影逛', '32'],
    'GuangChangMeiShiHuiTestCase'               : [u'广场美食汇', '33'],
    'GuangChangAiGouWuTestCase'                 : [u'广场爱购物', '34'],
    'GuangChangYouHuiTestCase'                  : [u'广场优惠', '38'],
    'HuiShengHuoRuKouTestCase'                  : [u'惠生活入口', '39'],
    'HuiShengHuoJingXuanTestCase'               : [u'惠生活精选/荐店', '41'],
    'FeiFanTongFuKuanTestCase'                  : [u'飞凡通付款', '42'],
    'FeiFanTongKaGuanJiaTestCase'               : [u'飞凡通卡管家', '43'],
    'FeiFanTongLingHuaQianTestCase'             : [u'飞凡通零花钱', '44'],
    'FeiFanTongZhangDanTestCase'                : [u'飞凡通账单', '45'],
    'FeiFanTongQiTaKuaiJieRuKouTestCase'        : [u'飞凡通其他快捷入口', '46'],
    'YaoYiYaoTestCase'                          : [u'摇一摇', '48'],
    'WoDeDengLuTestCase'                        : [u'我的登录', '49'],
    'WoDeGeRenXinXiTestCase'                    : [u'我的个人信息', '50'],
    'WoDePiaoQuanTestCase'                      : [u'我的票券', '51'],
    'WoDeDingDanTestCase'                       : [u'我的订单', '52'],
    'WoDeHuiYuanKaBaoTestCase'                  : [u'我的会员卡包', '53'],
    'WoDeFuKuanMaTestCase'                      : [u'我的付款码', '0'],
    'WoDeLingHuaQianTestCase'                   : [u'我的零花钱', '54'],
    'WoDeFeiFanTongTestCase'                    : [u'我的飞凡通', '55'],
    'WoDePaiDuiTestCase'                        : [u'我的排队', '57'],
    'WoDeTingCheJiaoFeiTestCase'                : [u'我的停车缴费', '58'],
    'WoDeSheZhiXiuGaiDengLuMiMaTestCase'        : [u'我的设置(修改登录密码)', '59-1'],
    'WoDeSheZhiXiuGaiZhiFuMiMaTestCase'         : [u'我的设置(修改支付密码)', '59-2'],
    'WoDeSheZhiXiuGaiXiaoEMianMiZhiFuTestCase'  : [u'我的设置(修改小额免密支付支付)', '59-3'],
    'WoDeXiaoXiZhongXinTestCase'                : [u'我的消息中心', '60'],
    'WoDeTuiChuTestCase'                        : [u'我的退出', '61'],
    'DengLuTestCase'                            : [u'登录', '1'],
    'TuiChuDengLuTestCase'                      : [u'退出登录', '2'],
    'RenYuanLieBiaoTestCase'                    : [u'人员列表', '3'],
    'XinZengYuanGongTestCase'                   : [u'新增员工', '4'],
    'BianJiYuanGongTestCase'                    : [u'编辑员工', '5'],
    'DongJieYuanGongTestCase'                   : [u'冻结员工', '6'],
    'JieDongYuanGongTestCase'                   : [u'解冻员工', '7'],
    'ShanChuYuanGongTestCase'                   : [u'删除员工', '8'],
    'JueSeLieBiaoTestCase'                      : [u'角色列表', '9'],
    'XinZengJueSeTestCase'                      : [u'新增角色', '10'],
    'LeFuZhangDanTestCase'                      : [u'乐付账单', '13'],
    'ShangXueYuanTestCase'                      : [u'商学院', '19']
}