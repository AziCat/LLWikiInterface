#coding=utf-8
#!/usr/bin/python
#Filename:F:/study/ssh/LL/src/LL/util/JsonUtil.py
# 对象转化为字典
def object2Dict(obj):
    d = {}
    d.update(obj.__dict__)
    return d