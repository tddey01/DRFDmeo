#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

"""
# 第一版 分页器
class MyPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    page_size_query_param = 'size' #
    max_page_size = 1     # 每页最大3个
"""

"""
# 第二版 分页器
class MyPagination(LimitOffsetPagination):

    default_limit = 1
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 1
"""


class MyPagination(CursorPagination):

    cursor_query_param = "cursor"
    page_size = 2
    ordering = "-id"