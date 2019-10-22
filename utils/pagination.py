#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from rest_framework.pagination import  PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    page_size_query_param = 'size' #
    max_page_size = 1     # 每页最大3个
