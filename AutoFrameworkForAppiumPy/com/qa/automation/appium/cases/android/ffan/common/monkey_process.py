'''
Created on Aug 31, 2016

@author: chencheng
'''

import os

class MonkeyHandle:
    def __init__(self,):
        self.dataMonkey = ""

        self.startTime = ''
        self.endTime = ''

        self.fileNameMoneky = 'Android_monkey.log'

    def Handle(self, startTime, endTime, reportPath='/Users/auto/Desktop/performance_data/'):
        try:
            self.startTime = startTime
            self.endTime = endTime
            monkeyFilePath = os.path.join(reportPath, self.fileNameMoneky)

            if(os.path.exists(monkeyFilePath)):
                self.monkeyHandle(monkeyFilePath)

            self.createHtmlReport(reportPath)

            # self.removePerformanceFile(monkeyFilePath)
        except Exception as e:
            print(str(e))

    def monkeyHandle(self, filePath):
        try:
            htmlContent = ''
            if filePath != '':
                number = 1
                monkeyData = self.dataHandle(filePath)
                crashLogs = ''
                for line in monkeyData:
                    crashLog = "<p>%s</p>" % line
                    crashLogs = crashLogs + crashLog
                    if line == '\n':
                        htmlContent = htmlContent + "<tr class='failClass'><td>%s</td><td>Crash Log</td><td><a href=\"javascript:showClassDetail('c%s',1)\">Detail</a></td></tr>" % (number, number)
                        htmlContent = htmlContent + "<tr id='ft%s.1' class='none hiddenRow'><td class='errorCase'><div class='testcase'>Crash Log</div></td><td colspan='5'>%s</td></tr>" % (number, crashLogs)
                        crashLogs = ''
                        number = number + 1

                if not htmlContent:
                    htmlContent = "<tr class='passClass'><td>%s</td><td colspan='3'>Pass</td></tr>" % number
                avgRowContent = ("<tr id='total_row'><td>total</td><td colspan='3'>%s Crash Infomation</td></tr>" % (number-1))
                htmlContent = htmlContent + avgRowContent
                self.dataMonkey = htmlContent
        except Exception as e:
            print(str(e))

    def dataHandle(self, filePath):
        monkeyData = []
        inseartValue = False
        dataFile = open(filePath, mode='r', encoding='utf-8')
        try:
            allLines = dataFile.readlines()
            for line in allLines:
                if line.startswith('// CRASH') or inseartValue == True:
                    monkeyData.append(line)
                    inseartValue = True
                    if line.startswith('**'):
                        inseartValue = False
                        monkeyData.append('\n')
        except Exception as e:
            raise
        finally:
            dataFile.close()

        return monkeyData

    def createHtmlReport(self, reportPath):
        report = os.path.join(reportPath, 'test_monkey_result.html')
        resultFile = open(report, 'w+')
        try:
            templateHtml = self.loadHtmlTemplate()
            monkeyData = self.dataMonkey

            templateHtml = templateHtml % (
            self.startTime, self.endTime, monkeyData)

            resultFile.write(templateHtml)
        except Exception as e:
            print(str(e))
        finally:
            resultFile.close()

    def createExcelReport(self):
        pass

    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateMonkey.html')
        templateFile = open(file)
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)

    def removePerformanceFile(self, filePath):
        try:
            if(os.path.exists(filePath)):
                os.remove(filePath)
        except Exception as e:
            print(str(e))


if (__name__ == "__main__"):
    # filePath = dict()
    # filePath['cpu']='/Users/auto/Desktop/performance_data/Cpu_performance.txt'
    # filePath['memory']='/Users/auto/Desktop/performance_data/Mem_peformance.txt'
    # filePath['coldboottime']='/Users/auto/Desktop/performance_data/ColdBootTime_com.wanda.app.wanhui_20160831110613.txt'
    # filePath['warmboottime']='/Users/auto/Desktop/performance_data/WarmBootTime_com.wanda.app.wanhui_20160831110613.txt'
    # filePath['fps']=''
    # filePath['rx']='/Users/auto/Desktop/performance_data/Rx_performance.txt'
    # filePath['tx']='/Users/auto/Desktop/performance_data/Tx_performance.txt'
    performance = MonkeyHandle()
    performance.Handle('2016/09/01 12:23', '2016/09/01 13:11', '/Users/yiceyun/work/autotest/android_monkey_log')
    # performance.removePerformanceFile('/Users/auto/Desktop/performance_data/Mem_com.wanda.app.wanhui_20160831173118.txt')
