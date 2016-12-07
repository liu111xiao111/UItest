import time
import requests
from configs import constants
from utility import mailProcess


def ctx_phone_get(ctx):
    url = "http://stat.intra.sit.ffan.com/getctxinfo?ctx='{0}'".format(ctx)
    print(ctx)
    try:
        response = requests.get(url=url,
                                data={ })
        response = eval(response.text)
        print(str(response))
        if response['msg'] == 'success':
            return response['phone']
    except Exception as e:
        print(str(e))
        return False

def sendMessage(phoneNumber, campaignMsg):
    validTime = int(time.time()) + 3600
    url = 'http://api.sit.ffan.com/msgcenter/v1/smsOutboxes'
    try:
        response = requests.post(url=url,
        data={'templateId':388,
        'deviceList':phoneNumber,
        'deviceType':0,
        'argsList':campaignMsg,
        'validTime':validTime,
        'contentType':0})
        response = eval(response.text)
        if response and response['message'] == 'OK':
            return 0
        else:
            return 1
    except Exception as e:
            print(str(e))
            return False

def sendTestResultMessage(deviceType):
    phonenums = constants.PhoneNumber.phoneNumberList
#     ctxUser = 'v_qiaojiaxi'
#     phoneCtx = ctx_phone_get(ctxUser)
#     if phoneCtx:
#         phonenums.append(phoneCtx)
    msg = '(商户)\n自动化回归测试-%s版(%s)：\n设备型号: %s \n系统版本: %s \n应用版本: %s \n开始时间: %s \n持续时间: %s \n总用例条数：%s \n成功个数：%s \n失败个数：%s \n错误个数：%s' % (deviceType, time.strftime('%Y-%m-%d'), mailProcess.DEVICE_TYPE, mailProcess.SYSTEM_VERSION, mailProcess.APP_VERSION, mailProcess.START_TIME, mailProcess.DURATION_TIME, mailProcess.TOTAL_TEST_CASES, mailProcess.PASS_TEST_CASES, mailProcess.FAIL_TEST_CASES, mailProcess.ERROR_TEST_CASES)
    for phonenum in phonenums:
        ret = sendMessage('[{0}]'.format(phonenum), '[["{0}","{0}","{1}"]]'.format('',msg))
        if ret== 1:
            resp = {
            'status': '500',
            'msg': '发送短信异常，请联系管理员。'
            }
            return


if __name__ == "__main__":
    sendTestResultMessage('Android')
