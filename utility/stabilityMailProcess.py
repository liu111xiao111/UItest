
import os
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from configs import constants


class StabilityHandle(object):
    def __init__(self, deviceType):

        if deviceType == 'android':
            from configs.androidConfig import appVersion, phoneVersion, buildVersion, deviceID
        elif deviceType == 'ios':
            from configs.iosConfig import appVersion, phoneVersion, buildVersion, deviceID
        else:
            raise

        self.appVersion = appVersion
        self.phoneVersion = phoneVersion
        self.buildVersion = buildVersion
        self.deviceID = deviceID

        self.startTime = ''
        self.endTime = ''

    def handle(self, startTime, endTime, reportPath):
        try:
            self.startTime = startTime
            self.endTime = endTime

            return self.generateReport()

        except Exception as e:
            print(str(e))

    def generateReport(self):
        try:
            templateHtml = self.loadHtmlTemplate()
            startTime = self.startTime
            endTime = self.endTime

            templateHtml = templateHtml % (self.phoneVersion, self.buildVersion, self.appVersion, 'WIFI', '0:13:16.436062', '10', '2', '1', '10', '20', '30', '10', '20', '30')
            print(templateHtml)
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
        reportFile = u'飞凡稳定性评测报告%s.xlsx' % time.strftime("%Y%m%d")
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
        msg['Subject'] = Header(constants.MONKEY_HEADR_NAME % (deviceType.capitalize(), time.strftime('%Y-%m-%d')), "utf-8")
    elif deviceType == 'ios':
        msg['Subject'] = Header(constants.MONKEY_HEADR_NAME % ('IOS', time.strftime('%Y-%m-%d')), "utf-8")
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
    reportPath = '/Users/uasd-qiaojx/Desktop/report/stability/20161216/9'
    sendTestResultMail('2016/09/01 12:23', '2016/09/01 13:11', reportPath, 'android')
