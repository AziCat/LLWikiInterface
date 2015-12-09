# -*- coding: UTF-8 -*-
#!/usr/bin/python
#Filename:F:/study/ssh/LL/src/LL/service/indexService.py
import requests
from LL.entity import Person
from bs4 import BeautifulSoup
#获取主页
mainPage = requests.get('http://www.lovelivewiki.com/w/%E9%A6%96%E9%A1%B5')
#转换成beautifulsoup对象
mainSoul = BeautifulSoup(mainPage.text)
#招募列表
recruitList = mainSoul.find_all('table','tab')[0].find_all('tr')
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
#获得当前招募，返回list[Person]
def getIndex():
    #{'nowRecruit':{'xxxx.png':'时间回复'},'nextRecruit':{}}
    recruitMap = {'nowRecruit':[],'nextRecruit':[]}
    #遍历本次招募列表
    for td in recruitList[0].find_all('td'):
        person = Person.__init__()
        if td.a is not None:
            person.img = td.a.img['src']
        else:
            person.img = td.text
        recruitMap['nowRecruit'].append(person)
    #遍历本次招募类型列表
    for i in range(len(recruitList[1].find_all('td'))):
        skill = recruitList[1].find_all('td')[i].text
        if recruitMap['nowRecruit'][i].img != '':
             recruitMap['nowRecruit'][i].skill = skill
        else:
             recruitMap['nowRecruit'][i+1].skill = skill

        
    #print recruitList[1].find_all('td')
    for i in range(len(recruitMap['nowRecruit'])-1):
        #去掉空对象
        if recruitMap['nowRecruit'][i].img == '':
            del recruitMap['nowRecruit'][i]
    return recruitMap['nowRecruit']

#获得下次招募，返回list[Person]
def getNextIndex():
    #{'nowRecruit':{'xxxx.png':'时间回复'},'nextRecruit':{}}
    recruitMap = {'nowRecruit':[],'nextRecruit':[]}
    #遍历下次招募列表
    for td in recruitList[2].find_all('td'):
        person = Person.__init__()
        if td.a is not None:
            person.img = td.a.img['src']
        else:
            person.img = td.text
        recruitMap['nextRecruit'].append(person)
    #遍历下次招募类型列表
    for i in range(len(recruitList[3].find_all('td'))):
        skill = recruitList[3].find_all('td')[i].text
        if recruitMap['nextRecruit'][i].img != '':
             recruitMap['nextRecruit'][i].skill = skill
        else:
             recruitMap['nextRecruit'][i+1].skill = skill

        
    #print recruitList[1].find_all('td')
    for i in range(len(recruitMap['nextRecruit'])-1):
        #去掉空对象
        if recruitMap['nextRecruit'][i].img == '':
            del recruitMap['nextRecruit'][i]
    return recruitMap['nextRecruit']