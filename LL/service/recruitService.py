# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
#获取模拟器页
mainPage = requests.get('http://www.lovelivewiki.com/w/11%E8%BF%9E%E6%A8%A1%E6%8B%9F%E5%99%A8')
#转换成beautifulsoup对象
mainSoul = BeautifulSoup(mainPage.text)
def getArgs():
    args = [];
    LBound = mainSoul.find(id='LBound').text
    RBound = mainSoul.find(id='RBound').text
    ACard = mainSoul.find(id='ACard').text
    BCard = mainSoul.find(id='BCard').text
    args.append({"LBound":LBound});
    args.append({"RBound":RBound});
    args.append({"ACard":ACard});
    args.append({"BCard":BCard});
    return args;