'''
Created on Aug 31, 2016

@author: chencheng
'''

import os
import time

class PerformanceHandle:
    def __init__(self):
        self.dataList = dict()

        self.dataList['cpu'] = ''
        self.dataList['memory'] = ''
        self.dataList['coldBoot'] = ''
        self.dataList['warmBoot'] = ''
        self.dataList['fps'] = ''
        self.dataList['rx'] = ''
        self.dataList['tx'] = ''

        self.columnNum = 2

        self.numBootEn = dict()
        self.numBootEn[1] = '1st'
        self.numBootEn[2] = '2nd'
        self.numBootEn[3] = '3rd'
        self.numBootEn[4] = '4th'
        self.numBootEn[5] = '5th'
        self.numBootEn[6] = '6th'
        self.numBootEn[7] = '7th'
        self.numBootEn[8] = '8th'
        self.numBootEn[9] = '9th'
        self.numBootEn[10] = '10th'

        self.startTime = ''
        self.endTime = ''

        self.fileNameCpu = 'Cpu_performance.txt'
        self.fileNameMemory = 'Mem_peformance.txt'
        self.fileNameFps = 'Fps_performance.txt'
        self.fileNameRx = 'Rx_performance.txt'
        self.fileNameTx = 'Tx_performance.txt'
        self.fileNameColdBootTime = 'ColdBootTime_performance.txt'
        self.fileNameWarmBootTime = 'WarmBootTime_performance.txt'

    def Handle(self, startTime, endTime, reportPath=''):
        try:
            self.startTime = startTime
            self.endTime = endTime
            cpuFilePath = os.path.join(reportPath, self.fileNameCpu)
            memoryFilePath = os.path.join(reportPath, self.fileNameMemory)
            coldBootFilePath = os.path.join(reportPath, self.fileNameColdBootTime)
            warmBootFilePath = os.path.join(reportPath, self.fileNameWarmBootTime)
            fpsFilePath = os.path.join(reportPath, self.fileNameFps)
            rxFilePath = os.path.join(reportPath, self.fileNameRx)
            txFilePath = os.path.join(reportPath, self.fileNameTx)

            if(os.path.exists(cpuFilePath)):
                self.cpuHandle(cpuFilePath)

            if (os.path.exists(memoryFilePath)):
                self.memoryHandle(memoryFilePath)

            if (os.path.exists(coldBootFilePath)):
                self.coldBootHandle(coldBootFilePath)

            if (os.path.exists(warmBootFilePath)):
                self.warmBootHandle(warmBootFilePath)

            if (os.path.exists(fpsFilePath)):
                self.fpsHandle(fpsFilePath)

            if (os.path.exists(rxFilePath)):
                self.rxHandle(rxFilePath)

            if (os.path.exists(txFilePath)):
                self.txHandle(txFilePath)

            self.createHtmlReport(reportPath)

            # self.removePerformanceFile(cpuFilePath)
            # self.removePerformanceFile(memoryFilePath)
            # self.removePerformanceFile(coldBootFilePath)
            # self.removePerformanceFile(warmBootFilePath)
            # self.removePerformanceFile(fpsFilePath)
            # self.removePerformanceFile(rxFilePath)
            # self.removePerformanceFile(txFilePath)

        except Exception as e:
            print(str(e))

    def cpuHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValues = []
            if(filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        if((i % self.columnNum) == 1):
                            rowContent = (
                            "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        htmlContent = htmlContent + rowContent

                        totalNum = totalNum + float(value[1])

                        listValues.append(float(value[1]))
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                if((i-1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                maxValue = max(listValues)
                minValue = min(listValues)
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['cpu'] = htmlContent
        except Exception as e:
            print(str(e))

    def memoryHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValues = []
            if (filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        if ((i % self.columnNum) == 1):
                            rowContent = (
                                "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        listValues.append(float(value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                if ((i - 1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                maxValue = max(listValues)
                minValue = min(listValues)
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['memory'] = htmlContent
        except Exception as e:
            print(str(e))

    def coldBootHandle(self, filePath):
        try:
            htmlContent = ""
            totalNum = 0
            listValue = []
            if (filePath != ''):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if(len(value) > 1):
                        rowContent = (
                        "<tr class='passClass'><td>%s</td><td>%s</td></tr>" % (self.numBootEn[i], value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        i = i + 1
                average = totalNum/10
                maxValue = max(listValue)
                minValue = min(listValue)
                avgRowContent = (
                "<tr id='total_row'><td>average/max/min</td><td>%s/%s/%s</td></tr>" % (average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['coldBoot'] = htmlContent
        except Exception as e:
            print(str(e))

    def warmBootHandle(self, filePath):
        try:
            htmlContent = ""
            totalNum = 0
            listValue = []
            if (filePath != ''):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if(len(value) > 1):
                        rowContent = (
                        "<tr class='passClass'><td>%s</td><td>%s</td></tr>" % (self.numBootEn[i], value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        i = i + 1
                average = totalNum/10
                maxValue = max(listValue)
                minValue = min(listValue)
                avgRowContent = (
                "<tr id='total_row'><td>average/max/min</td><td>%s/%s/%s</td></tr>" % (average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['warmBoot'] = htmlContent
        except Exception as e:
            print(str(e))

    def fpsHandle(self, filePath):
        try:
            htmlContent = ""
            if (filePath != ''):
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(' ')
                    if(len(value) > 1):
                        rowContent = (
                        "<tr class='passClass'><td>%s</td><td>%s</td><td>%s</td></tr>" % (value[0], value[1], value[2]))
                        htmlContent = htmlContent + rowContent
                self.dataList['fps'] = htmlContent
        except Exception as e:
            print(str(e))

    def rxHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValue = []
            if (filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        if ((i % self.columnNum) == 1):
                            rowContent = (
                                "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                maxValue = max(listValue)
                minValue = min(listValue)
                if ((i - 1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['rx'] = htmlContent
        except Exception as e:
            print(str(e))

    def txHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValue = []
            if (filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        if ((i % self.columnNum) == 1):
                            rowContent = (
                                "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                maxValue = max(listValue)
                minValue = min(listValue)
                if ((i - 1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['tx'] = htmlContent
        except Exception as e:
            print(str(e))

    def dataHandle(self, filePath):
        performanceData = []
        dataFile = open(filePath, mode='r', encoding='utf-8')
        try:
            allLines = dataFile.readlines()
            for line in allLines:
                performanceData.append(line)
        except Exception as e:
            raise
        finally:
            dataFile.close()

        return performanceData

    def createHtmlReport(self, reportPath):
        report = os.path.join(reportPath, 'test_performance_result.html')
        resultFile = open(report, 'w+')
        try:
            templateHtml = self.loadHtmlTemplate()
            cpuData = self.dataList['cpu']
            memoryData = self.dataList['memory']
            fpsData = self.dataList['fps']
            coldBootData = self.dataList['coldBoot']
            warmBootData = self.dataList['warmBoot']
            upstreamData = self.dataList['tx']
            downstreamData = self.dataList['rx']

            templateHtml = templateHtml % (
            self.startTime, self.endTime, cpuData, memoryData, fpsData, coldBootData, warmBootData, upstreamData, downstreamData)

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
        file = os.path.join(resourcesDirectory, 'templatePerformance.html')
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
    performance = PerformanceHandle()
    performance.Handle('2016/09/01 12:23', '2016/09/01 13:11', '/Users/auto/Desktop/performance_data')
    # performance.removePerformanceFile('/Users/auto/Desktop/performance_data/Mem_com.wanda.app.wanhui_20160831173118.txt')
