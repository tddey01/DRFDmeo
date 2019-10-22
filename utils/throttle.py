#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from rest_framework.throttling import BaseThrottle
import time

VISIT_RECORD = {}


class MyThrottle(BaseThrottle):

    def __init__(self):
        self.history = []

    def allow_request(self, request, view):
        # 实现限流的逻辑
        # 以IP访问
        # 访问列表 {IP:[tiem1,time2,time3]}
        # 获取请求的IP地址
        ip = request.META.get("REMOTE_ADDR")
        # 判断IP地址是否在访问列表
        print(ip,'IP')
        now = time.time()
        if ip not in VISIT_RECORD:
            #  不在 需要给访问列表添加key，value
            VISIT_RECORD[ip] = [now, ]
            return True
            #  在 需要把这个IP的访问记录 把当前时间加入到列表
        history = VISIT_RECORD[ip]
        history.insert(0, now)
        # 确保列表里最新访问时间以及最老的访问时间差 是1分钟
        while history and history[0] - history[-1] > 60:
            history.pop()
        self.history = history
        # 得到列表长度，判断是否是允许的次数
        if len(history) > 3:
            return False
        else:
            return True

    def wait(self):
        # 返回需要再等多久才能访问
        time = 60 - (self.history[0] - self.history[-1])
        return  time