'''
Created on Aug 31, 2016

@author: chencheng
'''

import os

class MonkeyHandle:
    def __init__(self,):
        self.dataMonkey = ""
        self.resultMonkey = ""

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
                exception = ''
                exception_list = {'空指针异常'      : 0,
                                  'debug异常'      : 0,
                                  '低内存异常'      : 0,
                                  '操作无响应异常'  : 0,
                                  '其他异常'        : 0}
                for line in monkeyData:
                    crashLog = "<p>%s</p>" % line
                    crashLogs = crashLogs + crashLog
                    if 'NullPointerException' in line:
                        exception = u'空指针异常'
                    elif 'IllegalStateException' in line:
                        exception = u'debug异常'
                    elif 'OutOfMemoryError' in line:
                        exception = u'低内存异常'
                    elif 'NOT RESPONDING' in line:
                        exception = u'操作无响应异常'
                    if line == '\n':
                        if exception == '':
                            exception = u'其他异常'
                        exception_list[exception] = exception_list[exception] + 1
                        htmlContent = htmlContent + "<tr class='failClass'><td>%s</td><td><a href=\"javascript:showClassDetail('c%s',1)\">Detail</a></td></tr>" % (exception, number)
                        htmlContent = htmlContent + "<tr id='ft%s.1' class='none hiddenRow'><td class='errorCase'><div class='testcase'>异常信息</div></td><td colspan='5'>%s</td></tr>" % (number, crashLogs)
                        crashLogs = ''
                        number = number + 1

                if not htmlContent:
                    htmlContent = "<tr class='passClass'><td>%s</td><td colspan='3'>Pass</td></tr>" % number
                self.dataMonkey = htmlContent

                avgRowContent = ''
                for key, value in exception_list.items():
                    avgRowContent = avgRowContent + "<tr id='result_row'><td>%s</td><td colspan='3'>%s</td></tr>" % (key, value)
                self.resultMonkey = avgRowContent
        except Exception as e:
            print(str(e))

    def dataHandle(self, filePath):
        monkeyData = []
        inseartValue = False
        dataFile = open(filePath, mode='r', encoding='utf-8')
        try:
            allLines = dataFile.readlines()
            for line in allLines:
                if line.startswith('// CRASH') or line.startswith('// NOT RESPONDING') or inseartValue == True:
                    inseartValue = True
                    if line == '\n':
                        continue
                    monkeyData.append(line)
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
            resultData = self.resultMonkey

            templateHtml = templateHtml % (
            self.startTime, self.endTime, monkeyData, resultData)

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
    performance = MonkeyHandle()
    performance.Handle('2016/09/01 12:23', '2016/09/01 13:11', '/Users/songbo')
