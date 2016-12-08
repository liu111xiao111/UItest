# -*- coding:utf-8 -*-

import sys, os
import time
from unittest import TestCase
from unittest import TestLoader
from unittest.suite import TestSuite

import HTMLTestRunner

from cases.ios.ffan.common.reportProcess import ReportHandle
from cases.ios.ffan.routing_inspection_test_cases.aiGouWu import AiGouWuTestCase
from cases.ios.ffan.routing_inspection_test_cases.banBenShengJi import BanBenShengJiTestCase
from cases.ios.ffan.routing_inspection_test_cases.chengShiQieHuan import ChenShiQieHuanTestCase
from cases.ios.ffan.routing_inspection_test_cases.dianYing import DianYingTestCase
from cases.ios.ffan.routing_inspection_test_cases.feiFanTongQITaRukou import FeiFanTongQitaRukouTestCase
from cases.ios.ffan.routing_inspection_test_cases.feiFanTongShiminGongjiaoka import FeiFanTongShiminGongjiaokaTestCase
from cases.ios.ffan.routing_inspection_test_cases.feiFanTongZhangDan import FeiFanTongZhangDanTestCase
from cases.ios.ffan.routing_inspection_test_cases.fuKuanMa import FuKuanMaTestCase
from cases.ios.ffan.routing_inspection_test_cases.gouWuZhongXin import GouWuZhongXinTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangDianYingGuang import GuangChangDianYingGuangTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangMaiDan import GuangChangMaiDanTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangMeiShiHui import GuangChangMeiShiHuiTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangSouSuo import GuangChangSouSuoTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangTingChe import GuangChangTingCheTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangXiangQing import GuangChangXiangQingTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangZhaoDian import GuangChangZhaoDianTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangZiYuanWei import GuangChangZiYuanWeiTestCase
from cases.ios.ffan.routing_inspection_test_cases.huiShengHuoRuKou import HuiShengHuoRuKouTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangHuiYuan import HuiYuanTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeLingHuaQian import LingHuaQianTestCase
from cases.ios.ffan.routing_inspection_test_cases.maiDan import MaiDanTestCase
from cases.ios.ffan.routing_inspection_test_cases.meiShiHui import MeiShiHuiTestCase
from cases.ios.ffan.routing_inspection_test_cases.mingDianYouPin import MingPinYouDianTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDePaiDui import PaiDuiTestCase
from cases.ios.ffan.routing_inspection_test_cases.paiDuiQuHao import PaiDuiQuHaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDePiaoQuan import PiaoQuanTestCase
from cases.ios.ffan.routing_inspection_test_cases.pinPaiJie import PinPaiJieTestCase
from cases.ios.ffan.routing_inspection_test_cases.qianDao import QianDaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.qinZi import QinZiTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoMenDian import QuanChengSouSuoMenDianTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoPinPai import QuanChengSouSuoPinPaiTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoShangPin import QuanChengSouSuoShangPinTestCase
from cases.ios.ffan.routing_inspection_test_cases.reCiSouSuo import ReCiSousuoTestCase
from cases.ios.ffan.routing_inspection_test_cases.shangChao import ShangChaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.shanPingShouYe import ShanPingShouYeTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangShiNeiDiTu import ShiNeiDiTuTestCase
from cases.ios.ffan.routing_inspection_test_cases.shouYeTingChe import ShouYeTingCheTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeDengLu import WoDeDengLuTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeDingDan import WoDeDingDanTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeFeiFanTong import WoDeFeiFanTongTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeGeRenXinXi import WoDeGeRenXinXiTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeHuiYuanKaBao import WoDeHuiYuanKaBaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeSheZhiMiMa import WoDeSheZhiMiMaTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeSheZhiXiaoEMianMi import WoDeSheZhiXiaoEMianMiTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeTingCheJiaoFei import WoDeTingCheJiaoFeiTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeTuiChu import WoDeTuiChuTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeXiaoXiZhongXin import WoDeXiaoXiZhongXinTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeXiHuan import WoDeXiHuanTestCase
from cases.ios.ffan.routing_inspection_test_cases.xianChangYao import XianChangYaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.yaoYiYao import YaoYiYaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.youHuiQuan import YouHuiQuanTestCase
from utility.messageProcess import sendTestResultMessage


from utility.mailProcess import sendTestResultMail



if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]


    # root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    # reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/auto/workspace_pycharm/autotest", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()

    # suite.addTest(ShanPingShouYeTestCase("test_case"))
    suite.addTest(QuanChengSouSuoPinPaiTestCase("test_case"))
    suite.addTest(QuanChengSouSuoShangPinTestCase("test_case"))
    suite.addTest(QuanChengSouSuoMenDianTestCase("test_case"))
    suite.addTest(ReCiSousuoTestCase("test_case"))
    suite.addTest(GouWuZhongXinTestCase("test_case"))
    # suite.addTest(DianYingTestCase("test_case"))
    # suite.addTest(MeiShiHuiTestCase("test_case"))
    suite.addTest(PinPaiJieTestCase("test_case"))
    # #suite.addTest(QinZiTestCase("test_case"))
    # suite.addTest(QianDaoTestCase("test_case"))
    suite.addTest(ChenShiQieHuanTestCase("test_case"))
    suite.addTest(ShangChaoTestCase("test_case"))
    suite.addTest(MingPinYouDianTestCase("test_case"))
    suite.addTest(ShouYeTingCheTestCase("test_case"))
    suite.addTest(MaiDanTestCase("test_case"))
    suite.addTest(GuangChangXiangQingTestCase("test_case"))
    suite.addTest(GuangChangSouSuoTestCase("test_case"))
    # suite.addTest(GuangChangZiYuanWeiTestCase("test_case"))
    suite.addTest(GuangChangZhaoDianTestCase("test_case"))
    # suite.addTest(YouHuiQuanTestCase("test_case"))
    # suite.addTest(XianChangYaoTestCase("test_case"))
    suite.addTest(PaiDuiQuHaoTestCase("test_case"))
    suite.addTest(ShiNeiDiTuTestCase("test_case"))
    suite.addTest(GuangChangTingCheTestCase("test_case"))
    suite.addTest(GuangChangMaiDanTestCase("test_case"))
    suite.addTest(HuiYuanTestCase("test_case"))
    # suite.addTest(GuangChangDianYingGuangTestCase("test_case"))
    suite.addTest(GuangChangMeiShiHuiTestCase("test_case"))
    # suite.addTest(AiGouWuTestCase("test_case"))
    # suite.addTest(HuiShengHuoRuKouTestCase("test_case"))
    # suite.addTest(FeiFanTongZhangDanTestCase("test_case"))
    # suite.addTest(FeiFanTongQitaRukouTestCase("test_case"))
    # suite.addTest(YaoYiYaoTestCase("test_case"))
    suite.addTest(WoDeDengLuTestCase("test_case"))
    suite.addTest(WoDeGeRenXinXiTestCase("test_case"))
    suite.addTest(PiaoQuanTestCase("test_case"))
    suite.addTest(WoDeDingDanTestCase("test_case"))
    suite.addTest(WoDeHuiYuanKaBaoTestCase("test_case"))
    suite.addTest(LingHuaQianTestCase("test_case"))
    suite.addTest(PaiDuiTestCase("test_case"))
    suite.addTest(WoDeTingCheJiaoFeiTestCase("test_case"))
    suite.addTest(WoDeXiaoXiZhongXinTestCase("test_case"))
    suite.addTest(WoDeTuiChuTestCase("test_case"))

    now = time.strftime('%H_%M_%S')

    filename = reportpath + 'feifan_automation_test_report_ios.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report_ios',
                                           description='Result for test')
    runner.run(suite)

    ReportHandle().handle(reportpath)

    if sentMail:
        sendTestResultMail(reportpath, 'ios')
        sendTestResultMessage('ios')
