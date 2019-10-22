#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from  rest_framework.throttling import  BaseThrottle

class MyTrottle(BaseThrottle):
    def allow_request(self, request, view):
        # 实现限流的逻辑
        pass

    def wait(self):
        # 需要等多久才能访问
        pass

