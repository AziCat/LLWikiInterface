# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from LL.util import DateUtil
from LL.entity import Line
#获取分数页
mainPage = requests.get('http://www.lovelivewiki.com/w/活动数据表')
#转换成beautifulsoup对象
mainSoul = BeautifulSoup(mainPage.text)


def getScroe():
    trs = mainSoul.find(id='eventData').find_all('tr')
    #图标tds
    iconTds = mainSoul.find(id='eventData').select("[rowspan~=4]")
    trlist = [];
    item = [];
    #划分每次活动的数据
    for index in range(len(trs)):
        total = index+1
        item.append(trs[index])
        #每4个一组
        if(total%4==0):
            trlist.append(item)
            item = []
    resultList = []
    #生成结果
    for index in range(len(trlist)):
        #时间数组
        timeArr = trlist[index][1].find_all('td')[0].text.split(' ')
        #去除时区内容  Mon Nov 16 2015 15:00:00 GMT+0800 (中国标准时间)
        del timeArr[-1]
        del timeArr[-1]
        #时间格式化
        time =  DateUtil.dateFormat(" ".join(timeArr))
        #头像
        icon = iconTds[index].find_all('img')[1]['src']
        #一档线
        oneLineArr = trlist[index][2].find_all('td')
        oneLine = []
        for item in oneLineArr:
            #如果是数字
            if item.text.isdigit():
                oneLine.append(item.text)
        #二档线
        twoLineArr = trlist[index][3].find_all('td')
        twoLine = []
        for item in twoLineArr:
            #如果是数字
            if item.text.isdigit():
                twoLine.append(item.text)
        #结果
        line = Line.__init__()
        line.icon = icon
        line.time = time
        line.oneLine = oneLine
        line.twoLine = twoLine
        resultList.append(line)
    return resultList