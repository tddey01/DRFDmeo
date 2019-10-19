from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from SerDemo import models



# Create your views here.

# book_list = [
#     {
#         'id:1,
#         'title':'xxx',
#     },{}
# ]

#
# class BookView(View):
#     # 第一版 用。values JsonResponse 实现序列化
#     # def get(self, request):
#     #     book_list = models.Book.objects.values("nid","title", "pub_time", 'publish')  # 获取数据
#     #     book_list = list(book_list)
#     #     ret = []
#     #     for book in book_list:
#     #         publisher_id = book["publish"]
#     #         publisher_obj = models.Publisher.objects.filter(nid=publisher_id).first()
#     #         book["publish"] = {
#     #             "id": publisher_id,
#     #             "title": publisher_obj.title
#     #         }
#     #         ret.append(book)
#     #     # ret = json.dumps(book_list,ensure_ascii=False)
#     #     # return HttpResponse(book_list)
#     #     return JsonResponse(ret, safe=False, json_dumps_params={"ensure_ascii": False})
#     # ========================================================================================================
#      第二版  用django serializers实现序列化
#     def get(self,request):
#         book_list = models.Book.objects.all()
#         ret =  serializers.serialize("json",book_list, ensure_ascii=False)
#         return  HttpResponse(ret)

from rest_framework.views import APIView
from rest_framework.response import  Response
from SerDemo import serializers

class BookView(APIView):

    def get(self,request):
        book_obj = models.Book.objects.first()
        ret = serializers.BookSerializer(book_obj)
        return  Response(ret.data)
