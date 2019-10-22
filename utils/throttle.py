#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from  rest_framework.throttling import  BaseThrottle

class MyTrottle(BaseThrottle):
    def allow_request(self, request, view):
        # 实现限流的逻辑
        # 以IP访问
        # 访问列表 {IP:[tiem1,time2,time3]}
        # 获取请求的IP地址
        # 判断IP地址是否在访问列表
            #  不在 需要给访问列表添加key，value
            #  在 需要把这个IP的访问记录 把当前时间加入到列表
        # 确保列表里最新访问时间以及最老的访问时间差 是1分钟
        # 得到列表长度，判断是否是允许的次数
        # 返回需要再等多久才能访问

        pass

    def wait(self):
        # 需要等多久才能访问
        pass

