from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.response import Response
from SerDemo import models
from  SerDemo import serializers

# Create your views here.

from rest_framework import  pagination
from utils.pagination import  MyPagination
class BookView(APIView):

    def get(self,request):
        queryset = models.Book.objects.all()
        # 实例化分页器对象
        page_obj = MyPagination()
        # 调用分页方法去分页queryset
        page_queryset = page_obj.paginate_queryset(queryset,request,view=self)
        # 把分页好的数据序列化返回

        # 带上上一页下一页连接的响应
        ser_obj = serializers.BookSerializer(page_queryset,many=True)

        # return Response(ser_obj.data)
        return page_obj.get_paginated_response(ser_obj.data)
       # http://127.0.0.1:8000/page/book?page=3 分页测试方法
