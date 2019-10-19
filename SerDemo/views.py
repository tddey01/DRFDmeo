from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic.base import View 
from SerDemo import models
import json
# Create your views here.

# book_list = [
#     {
#         'id:1,
#         'title':'xxx',
#     },{}
# ]


class BookView(View):
    
    def get(self,request):
        book_list = models.Book.objects.values('id','title')   # 获取数据
        book_list = list(book_list)
        ret = json.dumps(book_list,ensure_ascii=False)
        return  HttpResponse('ok')
