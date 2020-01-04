import xlrd
import TimeConverter
import time
import random

path = 'excel/courseData.xls'
random.seed(time.time)

def randOther(cur):
    random.seed(time.time)
    val = random.randint(0, 13)
    while val == cur:
        val = random.randint(0, 13)
    return val

class ExcelReader:
    timeCol = 1
    weekCol = 2
    placeCol = 3
    countCol = 4

    def __init__(self, path=path):
        self.path = path
        self.wb = xlrd.open_workbook(self.path)
        self.sheet = self.wb.sheet_by_index(0)
        self.nlines = self.nrows() - 2

        self.timeList = []
        self.weekNumList = []
        self.detTimeList = []
        self.weekList = []
        self.placeList = []

        self.items = {}
        self.itemCnt = 0

    def getNLines(self):
        return self.nlines

    def cell(self, row, col):
        return self.sheet.cell_value(row, col)

    def nrows(self):
        return self.sheet.nrows

    def ncols(self):
        return self.sheet.ncols

    # okay, this reader is for our course data specifically
    def summarizeTime(self, allVal=False, allWeekNum=False, allDetTime=False):
        c = ExcelReader.timeCol
        for i in range(self.nlines):
            r = i + 2
            val = self.cell(r, c).strip()
            if val != '' and (val not in self.timeList):
                self.timeList.append(val)
        if allVal:
            for v in self.timeList:
                print(v)
        if allWeekNum:
            for v in self.timeList:
                weekNum = v.split(' ')[0]
                if weekNum not in self.weekNumList:
                    self.weekNumList.append(weekNum)
                    print('{}: {}'.format(weekNum, TimeConverter.weekNumDict[weekNum]))
        if allDetTime:
            for v in self.timeList:
                detTime = v.split(' ')[1]
                detTime = detTime[1:len(detTime)-1]
                if detTime[-1] == '、':
                    detTime = detTime[:-1]
                detTime = detTime.strip().split('、')
                detTime = ((int)(detTime[0]), (int)(detTime[-1]))
                if detTime not in self.detTimeList:
                    self.detTimeList.append(detTime)
                    print(detTime)

    def summarizeWeek(self):
        c = ExcelReader.weekCol
        for i in range(self.nlines):
            r = i + 2
            val = self.cell(r, c).strip()
            if val != '' and (val not in self.weekList):
                self.weekList.append(val)
        for v in self.weekList:
            print(v)

    def summarizePlace(self):
        c = ExcelReader.placeCol
        for i in range(self.nlines):
            r = i + 2
            val = self.cell(r, c).strip()
            if val != '' and (val not in self.placeList):
                if val.find('荔园') != -1:
                    if 3 not in self.placeList:
                        self.placeList.append(3)
                elif val.find('创园') != -1:
                    if 2 not in self.placeList:
                        self.placeList.append(2)
                elif val.find('慧园') != -1 or val.find('润杨体育馆') != -1 or val.find('欣园网球场') != -1 or val.find('生物楼') != -1:
                    if 1 not in self.placeList:
                        self.placeList.append(1)
                elif val.find('一教') != -1 or val.find('二教') != -1 or val.find('一科') != -1 or val.find('检测中心') != -1 or val.find('分析测试中心') != -1:
                    if 13 not in self.placeList:
                        self.placeList.append(13)
                elif val.find('二科') != -1 or val.find('台州楼') != -1:
                    if 12 not in self.placeList:
                        self.placeList.append(12)
                elif val.find('棒球场') != -1:
                    if 8 not in self.placeList:
                        self.placeList.append(8)
                elif val.find('图书馆') != -1:
                    if 11 not in self.placeList:
                        self.placeList.append(11)
                elif val.find('游泳馆') != -1 or val.find('风雨操场') != -1 or val.find('书院学生乒乓球馆') != -1 or val.find('舞蹈房') != -1:
                    if 5 not in self.placeList:
                        self.placeList.append(5)
                elif val.find('松禾') != -1 or val.find('田径场') != -1:
                    if 6 not in self.placeList:
                        self.placeList.append(6)
                elif val.find('教工之家') != -1:
                    if 7 not in self.placeList:
                        self.placeList.append(7)
                else:
                    self.placeList.append(val)
        for v in self.placeList:
            print(v)

    def decodeTimeWindow(self, value, week):
        dayNum = value.split(' ')[0]
        dayNum = TimeConverter.weekNumDict[dayNum]
        detTime = value.split(' ')[1]
        detTime = detTime[1:len(detTime)-1]
        if detTime[-1] == '、':
            detTime = detTime[:-1]
        detTime = detTime.strip().split('、')
        detTime = ((int)(detTime[0]), (int)(detTime[-1]))
        early = TimeConverter.timestamp(week, dayNum, detTime[0]-1, point='end')
        late = TimeConverter.timestamp(week, dayNum, detTime[0], point='start')
        preTimeWindow = (early, late)
        early = TimeConverter.timestamp(week, dayNum, detTime[1], point='end')
        late = TimeConverter.timestamp(week, dayNum, detTime[1]+1, point='start')
        postTimeWindow = (early, late)
        return {'pre': preTimeWindow, 'post':postTimeWindow, 'day': dayNum}

    def decodeWeek(self, value):
        values = value.split(',')
        weeks = []
        for val in values:
            hasHr = val.find('-') != -1
            if hasHr:
                sessions = val.split('-')
                begin = (int)(sessions[0])
                end = (int)(sessions[1])
                for i in range(begin, end+1):
                    if i not in weeks:
                        weeks.append(i)
            else:
                week = (int)(val)
                if week not in weeks:
                    weeks.append(week)
        return weeks

    def decodePlace(self, value):
        if value.find('荔园') != -1:
            return 3
        elif value.find('创园') != -1:
            return 2
        elif value.find('慧园') != -1 or value.find('润杨体育馆') != -1 or value.find('欣园网球场') != -1 or value.find('生物楼') != -1:
            return 1
        elif value.find('一教') != -1 or value.find('二教') != -1 or value.find('一科') != -1 or value.find('检测中心') != -1 or value.find('分析测试中心') != -1:
            return 13
        elif value.find('二科') != -1 or value.find('台州楼') != -1:
            return 12
        elif value.find('棒球场') != -1:
            return 8
        elif value.find('图书馆') != -1:
            return 11
        elif value.find('游泳馆') != -1 or value.find('风雨操场') != -1 or value.find('书院学生乒乓球馆') != -1 or value.find('舞蹈房') != -1:
            return 5
        elif value.find('松禾') != -1 or value.find('田径场') != -1:
            return 6
        elif value.find('教工之家') != -1:
            return 7
        else:   # start from Gate 1 plz, never heard of it...
            return 10

    def decodeItems(self):
        self.items = {}
        self.itemCnt = 0
        for i in range(self.nlines):
            r = i + 2
            # weeks first
            weekVal = self.cell(r, ExcelReader.weekCol).strip()
            if weekVal == '':
                continue
            weeks = self.decodeWeek(weekVal)
            # now place
            placeVal = self.cell(r, ExcelReader.placeCol).strip()
            if placeVal == '':
                continue
            place = self.decodePlace(placeVal)
            # now count
            count = (int)(self.cell(r, ExcelReader.countCol))
            # finally time window
            timeVal = self.cell(r, ExcelReader.timeCol).strip()
            for student in range(count):
                for week in weeks:
                    if week not in self.items:
                        self.items[week] = {}
                    timeWindow = self.decodeTimeWindow(timeVal, week)
                    day = timeWindow['day']
                    if day not in self.items[week]:
                        self.items[week][day] = []
                    preW = timeWindow['pre']
                    preLoc = randOther(place)
                    item = (preLoc, place, preW[0], preW[1])
                    # print(item)
                    self.items[week][day].append(item)
                    self.itemCnt += 1
                    postW = timeWindow['post']
                    postLoc = randOther(place)
                    item = (place, postLoc, postW[0], postW[1])
                    # print(item)
                    self.items[week][day].append(item)
                    self.itemCnt += 1
        print('ok, got {} items.'.format(self.itemCnt))

if __name__ == '__main__':
    er = ExcelReader(path)
    # print(er.getNLines())
    # er.summarizeTime(allDetTime=True)
    # er.summarizeWeek()
    # er.summarizePlace()
    er.decodeItems()
