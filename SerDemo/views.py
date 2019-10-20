from django.shortcuts import render
from SerDemo import models



# Create your views here.

# book_list = [
#     {
#         'id:1,
#         'title':'xxx',
#     },{}
# ]

# from django.views.generic.base import View
# class BookView(View):
#     # 第一版 用。values JsonResponse 实现序列化
#     # from django.http import JsonResponse, HttpResponse
#     # from SerDemo import models
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
#     from django.core import serializers
#     from django.http import JsonResponse, HttpResponse
#     from SerDemo import models
#     def get(self,request):
#         book_list = models.Book.objects.all()
#         ret =  serializers.serialize("json",book_list, ensure_ascii=False)
#         return  HttpResponse(ret)

'''
# DRF 第一版
from rest_framework.views import APIView
from rest_framework.response import  Response
from SerDemo import serializers
from SerDemo import models

class BookView(APIView):

    def get(self,request):
        book_obj = models.Book.objects.first()
        ret = serializers.BookSerializer(book_obj)
        return  Response(ret.data)
'''

'''
# DRF 第二版
from rest_framework.views import APIView
from rest_framework.response import  Response
from SerDemo import serializers
from SerDemo import models

class BookView(APIView):

    def get(self,request):
        book_list = models.Book.objects.all()
        ret = serializers.BookSerializer(book_list,many=True) # many=True 代表传多个参数
        return  Response(ret.data)
'''

# '''
# DRF 第三版
from rest_framework.views import APIView
from rest_framework.response import  Response
from SerDemo import serializers
from SerDemo import models

class BookView(APIView):

    def get(self,request):
        book_list = models.Book.objects.all()
        ret = serializers.BookSerializer(book_list,many=True) # many=True 代表传多个参数
        return  Response(ret.data)

    def post(self,request):
        print(request.data)
        serializer = serializers.BookSerializer(data=request.data)   # 传入反序列数据
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)

# '''

class BookEditView(APIView):

    def get(self,request,id):  # 查看单条数据
        book_obj = models.Book.objects.filter(nid=id).first()
        ret = serializers.BookSerializer(book_obj)

        return Response(ret.data)

    def put(self,request,id):
        print(request.data)
        book_obj = models.Book.objects.filter(nid=id).first()
        serializer = serializers.BookSerializer(book_obj,data=request.data,partial=True)  # partial=True  允许部分更新
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)
