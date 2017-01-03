import os
import time
import datetime
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from configs import constants


class StabilityHandle(object):
    def __init__(self, deviceType):

        if deviceType == 'android':
            from configs.androidConfig import appVersion, phoneVersion, buildVersion, deviceID, deviceNet, stabilityTestCaseNumber
            from tools.utility.constants import OUTLOOPNUM, INSIDELOOPNUM
            from tools.stabilityHandler import ANR_ERROR, JNT_ERROR, JNT_CRASH, APP_DIED, SYSTEM_ERROR
        elif deviceType == 'ios':
            from configs.iosConfig import appVersion, phoneVersion, buildVersion, deviceID
        else:
            raise

        self.appVersion = appVersion
        self.phoneVersion = phoneVersion
        self.buildVersion = buildVersion
        self.deviceID = deviceID
        self.deviceNet = deviceNet
        self.stabilityTestCaseNumber = stabilityTestCaseNumber
        self.loopNumber = OUTLOOPNUM * INSIDELOOPNUM

        self.anrError = ANR_ERROR
        self.jntError = JNT_ERROR
        self.jntCrash = JNT_CRASH
        self.appDied = APP_DIED
        self.systemError = SYSTEM_ERROR
        self.totalCrash = self.anrError + self.jntCrash
        self.totalError = self.anrError + self.jntError + self.jntCrash + self.appDied + self.systemError

    def handle(self, startTime, endTime, reportPath):
        try:
            date1 = time.strptime(startTime,"%Y/%m/%d %H:%M:%S")
            date2 = time.strptime(endTime,"%Y/%m/%d %H:%M:%S")
            date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
            date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
            self.duration = date2 - date1

            return self.generateReport()

        except Exception as e:
            print(str(e))

    def generateReport(self):
        try:
            templateHtml = self.loadHtmlTemplate()
            templateHtml = templateHtml % (self.phoneVersion, self.buildVersion,\
                                           self.appVersion, self.deviceNet, self.duration,\
                                           self.stabilityTestCaseNumber, self.loopNumber,\
                                           self.totalCrash, self.anrError, self.jntError,\
                                           self.jntCrash, self.appDied, self.systemError, self.totalError)
            return templateHtml
        except Exception as e:
            print(str(e))

    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateMailStability.html')
        templateFile = open(file, encoding='utf-8')
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)

def sendTestResultMail(startTime, endTime, reportPath, deviceType):
    fromAddress = constants.Email.mailAddress
    toAddress = constants.Email.monkeyMaillAddress
    smtpServer = constants.Email.smtpServer
    smtpUser = constants.Email.username
    smtpPassword = constants.Email.password
    smtpPort = constants.Email.smtpPort

    attachmentFiles = []

    if deviceType == 'android':
        logcatFile = 'log.zip'
        reportFile = u'飞凡APP重点功能压力测试报告(%s).xlsx' % time.strftime("%Y%m%d")
        attachmentFiles.append(reportFile)
        attachmentFiles.append(logcatFile)
    elif deviceType == 'ios':
        pass
    else:
        raise

    mailBodyContents = StabilityHandle(deviceType).handle(startTime, endTime, reportPath)
    msg = MIMEMultipart('related')

    body = MIMEText(mailBodyContents, 'html', 'utf-8')
    msg.attach(body)

    attachmentPath = os.path.join(reportPath, 'attachment')
    for file in attachmentFiles:
        filePath = os.path.join(attachmentPath, file)
        if os.path.exists(filePath):
            attach = MIMEApplication(open(filePath, 'rb').read())
            attach.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(attach)

    if deviceType == 'android':
        msg['Subject'] = Header(constants.STABILITY_HEADR_NAME % (deviceType.capitalize(), time.strftime('%Y%m%d')), "utf-8")
    elif deviceType == 'ios':
        msg['Subject'] = Header(constants.STABILITY_HEADR_NAME % ('IOS', time.strftime('%Y%m%d')), "utf-8")
    else:
        raise
    msg['From'] = (r"%s <" + fromAddress + ">") % Header(constants.SYSTEM_NAME, "utf-8")
    msg['To'] = ';'.join(toAddress)

    s = smtplib.SMTP(smtpServer, smtpPort)
    s.ehlo()
    s.starttls()
    s.login(smtpUser, smtpPassword)
    s.sendmail(fromAddress, toAddress, msg.as_string())
    s.quit()


if __name__ == "__main__":
    reportPath = '/Users/uasd-qiaojx/Desktop/report/stability/20161229/10'
    sendTestResultMail('2016/12/29 16:54:36', '2016/12/29 18:13:08', reportPath, 'android')
