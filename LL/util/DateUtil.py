#coding=utf-8
#!/usr/bin/python
#Filename:F:/study/ssh/LL/src/LL/util/DateUtil.py
#时间工具类
import datetime
#dateStr格式：Fri Aug 14 2015 15:00:00
#返回 2015-4-14
def dateFormat(dateStr):
    dd=datetime.datetime.strptime(dateStr,'%a %b %d %Y %H:%M:%S')
    return dd.strftime('%Y-%m-%d')
