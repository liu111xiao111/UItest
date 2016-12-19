# -*- coding: utf-8 -*-

from utility.device_info_util import DeviceInfoUtil

appVersion = '4.10.0.1260'

phoneVersion = DeviceInfoUtil().getIPhoneType()

buildVersion = DeviceInfoUtil().getIProductVersion()

deviceID = DeviceInfoUtil().getUdid()

deviceNet = 'WIFI'

caseList = {
    # 'ShanPingShouYeTestCase'                        : [u'闪屏首页', '1'],
     'ChenShiQieHuanTestCase'                        : [u'城市切换', '2'],
     'QuanChengSouSuoPinPaiTestCase'                 : [u'全城搜索(品牌)', '3-1'],
     'QuanChengSouSuoShangPinTestCase'               : [u'全城搜索(商品)', '3-2'],
     'QuanChengSouSuoMenDianTestCase'                : [u'全城搜索(门店)', '3-3'],
     'ReCiSousuoTestCase'                            : [u'热词搜索', '4'],
     'GouWuZhongXinTestCase'                         : [u'购物中心', '5'],
    # 'DianYingTestCase'                              : [u'电影', '6'],
    # 'MeiShiHuiTestCase'                             : [u'美食汇', '7'],
     'PinPaiJieTestCase'                             : [u'品牌街', '8'],
    # 'QinZiTestCase'                                 : [u'亲子', '9'],
    # 'QianDaoTestCase'                               : [u'签到', '10'],
     'ShangChaoTestCase'                             : [u'商超', '11'],
     'MingPinYouDianTestCase'                        : [u'名店优品', '14'],
     'ShouYeTingCheTestCase'                         : [u'首页停车', '16'],
     'MaiDanTestCase'                                : [u'买单', '17'],
     'GuangChangXiangQingTestCase'                   : [u'广场详情', '21'],
     'GuangChangSouSuoTestCase'                      : [u'广场搜索', '22'],
    # 'GuangChangZiYuanWeiTestCase'                   : [u'广场资源位', '23'],
     'GuangChangZhaoDianTestCase'                    : [u'广场找店', '24'],
    # 'YouHuiQuanTestCase'                            : [u'广场优惠券', '25'],
    # 'XianChangYaoTestCase'                          : [u'广场现场摇', '26'],
     'PaiDuiQuHaoTestCase'                           : [u'广场排队取号', '27'],
     'ShiNeiDiTuTestCase'                            : [u'广场室内地图', '28'],
     'GuangChangTingCheTestCase'                     : [u'广场停车', '29'],
     'GuangChangMaiDanTestCase'                      : [u'广场买单', '30'],
     'HuiYuanTestCase'                               : [u'广场会员', '31'],
    # 'GuangChangDianYingGuangTestCase'               : [u'广场电影逛', '32'],
     'GuangChangMeiShiHuiTestCase'                   : [u'广场美食汇', '33'],
    # 'AiGouWuTestCase'                               : [u'广场爱购物', '34'],
    # 'HuiShengHuoRuKouTestCase'                      : [u'慧生活入口', '39'],
    # 'FeiFanTongZhangDanTestCase'                    : [u'飞凡通账单', '45'],
    # 'FeiFanTongQitaRukouTestCase'                   : [u'飞凡通其他快捷入口', '46'],
    # 'YaoYiYaoTestCase'                              : [u'摇一摇', '48'],
     'WoDeDengLuTestCase'                            : [u'我的登录', '49'],
     'WoDeGeRenXinXiTestCase'                        : [u'我的个人信息', '50'],
     'PiaoQuanTestCase'                              : [u'我的票券', '51'],
     'WoDeDingDanTestCase'                           : [u'我的订单', '52'],
     'WoDeHuiYuanKaBaoTestCase'                      : [u'我的会员卡包', '53'],
    # 'FuKuanMaTestCase'                              : [u'我的付款码', '0'],
     'LingHuaQianTestCase'                           : [u'我的零花钱', '54'],
    # 'WoDeFeiFanTongTestCase'                        : [u'我的飞凡通', '55'],
    # 'WoDeXiHuanTestCase'                            : [u'我的喜欢', '56'],
     'PaiDuiTestCase'                                : [u'我的排队', '57'],
     'WoDeTingCheJiaoFeiTestCase'                    : [u'我的停车缴费', '58'],
    # 'WoDeSheZhiXiaoEMianMiTestCase'                 : [u'我的设置(小额免密设置)', '59-1'],
    # 'WoDeSheZhiMiMaTestCase'                        : [u'我的设置(修改密码)', '59-2'],
     'WoDeXiaoXiZhongXinTestCase'                    : [u'我的消息中心', '60'],
     'WoDeTuiChuTestCase'                            : [u'我的退出', '61'],
    # 'FeiFanTongShiminGongjiaokaTestCase'            : [u'飞凡通市民/公交卡', '62'],
    # 'BanBenShengJiTestCase'                         : [u'版本升级', '63'],




     # 商户 case
     'BianJiYuanGong'    :    [u'编辑员工','1'],
     'DenggLuCase'    :    [u'登录','2'],
     'DongJieYuanGong'    :    [u'冻结员工','3'],
     'JiaoYiGuanBiDingDan'    :    [u'交易关闭订单','4'],
     'JieDongYuanGong'    :    [u'解冻员工','5'],
     'JueSeLieBiao'    :    [u'角色列表','6'],
     'QuanBuDingDanZhuangTai'    :    [u'全部订单状态','7'],
     'RenYuanLieBiao'    :    [u'人员列表','8'],
     'TuiChuDengLuCase'    :    [u'退出登录','9'],
     'XianShiQiangGouXiangXi'    :    [u'限时抢购详细','10'],
     'XinZengJueSe'    :    [u'新增角色','11'],
     'XinZengYuanGongCase'    :    [u'新增员工','12'],
     'ShangXueYuanRuKou'    :    [u'商学院入口','13'],


}
