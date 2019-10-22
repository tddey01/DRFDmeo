#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from rest_framework import versioning


class MyVersion():

    def determine_version(self, request, *args, **kwargs):
        '''
        :param request:  返回值 给了request.version
        :param args:  返回版本号
        :param kwargs:  版本号携带在过滤条件 xxxx?version=v1
        :return:
        '''

        version = request.query_params.get("version", "v1")

        return version
