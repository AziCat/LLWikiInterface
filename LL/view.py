#coding=utf-8
#!/usr/bin/python
#Filename:F:/study/ssh/LL/src/LL/view.py
from django.http import HttpResponse
from LL.service import indexService,eventService,recruitService,scroeLineService
import json
from LL.util import JsonUtil
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
def Hello(req):
    return HttpResponse('<h1>hello world!</h1>')

def compute(req):
    x = req.GET.get('x')
    y = req.GET.get('y')
#     try:
    result = int(x)+int(y)
#     except:
#         raise Http404
    return HttpResponse('x+y='+str(result))
def main(req):
    """
    <table>
        <tr>
            <td>本次招募</td><td><img src=''></td>
        </tr>
    </table>
    """
    """
    josn:
    [
        {"img":""},
        {"img":""}
    ]
    """
    resultList = indexService.getNextIndex()
    jsonList = []
    page = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><table><tr>'
    for person in resultList:
        jsonList.append(JsonUtil.object2Dict(person))
        if '招募' in person.img:
            page+='<td>本次招募</td>'
        else:
            page+='<td><img src='+person.img+'></td>'
    page+='</tr><tr>'
    for person in resultList:
        if '招募' in person.img:
            page+='<td>技能</td>'
        else:
            page+='<td>'+person.skill+'</td>'
    page+='</tr></table>'
    page+='</br>json:'+ json.dumps(jsonList).decode("unicode-escape") 
    return HttpResponse(page)

#获取当前招募Json
def getNowRecruit(req):
    resultList = indexService.getIndex()
    jsonList = []
    for person in resultList:
        jsonList.append(JsonUtil.object2Dict(person))
    return HttpResponse(json.dumps(jsonList).decode("unicode-escape"))
#获取下次招募Json
def getNextRecruit(req):
    resultList = indexService.getNextIndex()
    jsonList = []
    for person in resultList:
        jsonList.append(JsonUtil.object2Dict(person))
    return HttpResponse(json.dumps(jsonList).decode("unicode-escape"))   
#活动列表
def getEventList(req):
    eventList = eventService.getEventList()
    jsonList = []
    for event in eventList:
        jsonList.append(JsonUtil.object2Dict(event))
    return HttpResponse(json.dumps(jsonList).decode("unicode-escape"))
#模拟招募参数
def getRecruitArgs(req):
    args = recruitService.getArgs();
    return HttpResponse(json.dumps(args).decode("unicode-escape"))
def getScroe(req):
    resultList = scroeLineService.getScroe()
    jsonList = []
    for person in resultList:
        jsonList.append(JsonUtil.object2Dict(person))
    return HttpResponse(json.dumps(jsonList).decode("unicode-escape"))