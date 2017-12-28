
import time
import requests



class MessageTest():
    def msg_send(phoneNumber, campaignMsg):
        validTime = int(time.time()) + 3600

        url = 'http://api.sit.ffan.com/msgcenter/v1/smsOutboxes'
        try:
            response = requests.post(url=url,
                                 data={'templateId': 388,
                                       'deviceList': phoneNumber,
                                       'deviceType': 0,
                                       'argsList': campaignMsg,
                                       'validTime': validTime,
                                       'contentType': 0})
            response = eval(response.text)
            if response and response['message'] == 'OK':
                return 0
            else:
                return 1
        except Exception as e:
            print(str(e))

        return False



    def send_msg(self,phone_number_arrs,msg):
        for phonenum in phone_number_arrs:
            ret = MessageTest.msg_send('[{0}]'.format(phonenum), '[["{0}","{0}","{1}"]]'.format('', msg))
        if ret == 1:
            resp = {
                'status': '500',
                'msg': '发送短信异常，请联系管理员。'
            }
        return

if __name__ == "__main__":
    data = time.strftime('%Y-%m-%d')
    #suite = TestLoader().loadTestsFromTestCase(InspectorTimeout)
    DEVICE_TYPE = 'iPhone6S'
    SYSTEM_VERSION = '9.3.2'

    # #商户
    # APP_VERSION = '1.7.18'
    # START_TIME = '%s 04:05:01' % data
    # DURATION_TIME = '0:18:13.706269'
    # TOTAL_TEST_CASES = '13'
    # PASS_TEST_CASES = '13'
    # FAIL_TEST_CASES = '0'
    # ERROR_TEST_CASES = '0'

    #phoneNumberArrs = ['13910236830', '17704111698', '18624264849', '13504286090', '15040493615']
    phoneNumberArrs = ['13504286090']
    #
    # msg = '(商户)\n自动化回归测试-%s版(%s)：\n设备型号: %s \n系统版本: %s \n应用版本: %s \n开始时间: %s \n持续时间: %s \n总用例条数：%s \n成功个数：%s \n失败个数：%s \n错误个数：%s' % (
    # #msg = '\n自动化回归测试-%s版(%s)：\n设备型号: %s \n系统版本: %s \n应用版本: %s \n开始时间: %s \n持续时间: %s \n总用例条数：%s \n成功个数：%s \n失败个数：%s \n错误个数：%s' % (
    # 'iOS', time.strftime('%Y-%m-%d'), DEVICE_TYPE, SYSTEM_VERSION, APP_VERSION,
    # START_TIME, DURATION_TIME, TOTAL_TEST_CASES, PASS_TEST_CASES,
    # FAIL_TEST_CASES, ERROR_TEST_CASES)
    #
    # MessageTest().send_msg(phoneNumberArrs,msg)

    APP_VERSION = '4.11.1.1291'
    START_TIME = '%s 02:40:01' % data
    DURATION_TIME = '0:32:25.433375'
    TOTAL_TEST_CASES = '30'
    PASS_TEST_CASES = '30'
    FAIL_TEST_CASES = '0'
    ERROR_TEST_CASES = '0'

    msg = '\n自动化回归测试-%s版(%s)：\n设备型号: %s \n系统版本: %s \n应用版本: %s \n开始时间: %s \n持续时间: %s \n总用例条数：%s \n成功个数：%s \n失败个数：%s \n错误个数：%s' % (
        'iOS', time.strftime('%Y-%m-%d'), DEVICE_TYPE, SYSTEM_VERSION, APP_VERSION,
        START_TIME, DURATION_TIME, TOTAL_TEST_CASES, PASS_TEST_CASES,
        FAIL_TEST_CASES, ERROR_TEST_CASES)

    MessageTest().send_msg(phoneNumberArrs, msg)