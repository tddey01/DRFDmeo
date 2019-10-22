#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from rest_framework.exceptions import  AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from authDemo import  models


class MyAuth(BaseAuthentication):
    def authenticate(self,request):
        # 看他是否登录成功
        # 从url过滤条件拿到token
        # 去数据库看token 是否合法
        token = request.query_params.get('token','')
        if not token:
            raise  AuthenticationFailed("没有携带token")
        user_obj = models.User.objects.filter(token=token).first()
        if  not user_obj:
            raise AuthenticationFailed("token不合")

        # return (None,None)
        return (user_obj,token)