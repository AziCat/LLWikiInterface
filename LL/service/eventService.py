# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from LL.entity import Event
#获取活动列表页
mainPage = requests.get('http://www.lovelivewiki.com/w/EventList')
#转换成beautifulsoup对象
mainSoul = BeautifulSoup(mainPage.text)
def test():
    tr01 = mainSoul.find(id='EventList').find_all('tr')[9]
    print 'style='+tr01['style']
    tds = tr01.find_all('td')
    print 'id='+tds[0].text
    print '活动名='+tds[1].a['title']
    print '时间='+tds[2].text
    print '活动曲='+tds[4].text
    print '档线='+tds[5].text+'/'+tds[6].text

def getEventList():
    eventList = [];
    #获取内容
    trs = mainSoul.find(id='EventList').find_all('tr')
    for i in range(len(trs)):
        if 0 == i:
            continue
        #创建活动对象
        event = Event.__init__()
        try:
            #如果有样式，活动已结束或者进行中
            if trs[i]['style'] is not None:
                #进行中
                if 'background' in trs[i]['style'] > 0 :
                    event.isActive = True
                    event.isOver = False
                #已结束
                else :
                    event.isActive = False
                    event.isOver = True
            #获取tds
            tds = trs[i].find_all('td')
            event.personId = tds[0].text.strip()
            event.eventName = tds[1].a['title'].strip()
            event.eventTime = tds[2].text.strip()
            #是否SM
            try:
                event.eventSong = tds[4].a['title'].strip()
            except:
                event.eventSong = '略'
            event.line = tds[5].text.strip()+'/'+tds[6].text.strip() 
        except:
            #如果没样式
            event.isActive = False
            event.isOver = False
            tds = trs[i].find_all('td')
            #判断是否是空行
            if tds[0].text.strip() == '':
                #跳过
                continue
            else:
                event.personId = tds[0].text.strip()
                #判断是否包含链接
                try:
                    event.eventName = tds[1].a['title'].strip()
                except:
                    event.eventName = tds[1].text.strip()
                event.eventTime = tds[2].text.strip()
                #是否SM
                try:
                    event.eventSong = tds[4].a['title'].strip()
                except:
                    event.eventSong = '略'
                event.line = tds[5].text.strip()+'/'+tds[6].text.strip()
        eventList.append(event)
    return eventList