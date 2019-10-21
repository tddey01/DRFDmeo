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

"""
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
"""

"""
# DRF 第四版 第一次封装视图函数
from rest_framework.views import APIView
from rest_framework.response import Response
from SerDemo import serializers
from SerDemo import models


class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):

    def list(self, request):
        queryset = self.get_queryset()
        ret = self.get_serializer(queryset, many=True)
        return Response(ret.data)


class CreateModelMixin(object):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        ret = self.get_serializer(book_obj)
        return Response(ret.data)


class PutModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)  # partial=True  允许部分更新
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DelModelMixin(object):
    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        book_obj.delete()
        return Response('delete')

class BookView(GenericAPIView, ListModelMixin, CreateModelMixin):
   
    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request):   # 查看数据
        return self.list(request)

    def post(self, request): # 添加数据
        return self.create(request)


class BookEditView(GenericAPIView, RetrieveModelMixin,PutModelMixin,DelModelMixin):
    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request, id):  # 查看单条数据
        return self.retrieve(request, id)

    def put(self, request, id):   # 修改数据
        return self.update(request,id)

    def delete(self, request, id): # 删除数据
        return self.destroy(request,id)
"""

"""
# DRF 第五版 第二次封装视图函数
from rest_framework.views import APIView
from rest_framework.response import Response
from SerDemo import serializers
from SerDemo import models


class GenericAPIView(APIView):

    query_set = None
    serializer_class = None

    def get_queryset(self):
        '''

        :return:
        '''
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        '''

        :param args:
        :param kwargs:
        :return:
        '''
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):

    def list(self, request):
        queryset = self.get_queryset()
        ret = self.get_serializer(queryset, many=True)
        return Response(ret.data)


class CreateModelMixin(object):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ListCreateModelMixiin(GenericAPIView, ListModelMixin, CreateModelMixin):
    pass

class BookView(ListCreateModelMixiin):

    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request):   # 查看数据
        '''

        :param request:
        :return:
        '''
        return self.list(request)

    def post(self, request): # 添加数据
        '''

        :param request:
        :return:
        '''
        return self.create(request)



class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        ret = self.get_serializer(book_obj)
        return Response(ret.data)


class UpdateModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)  # partial=True  允许部分更新
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DestroyModelMixin(object):

    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        book_obj.delete()
        return Response('delete')


class RetrieveUpdateDestroyAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass



class BookEditView(RetrieveUpdateDestroyAPIView):


    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request, id):  # 查看单条数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.retrieve(request, id)

    def put(self, request, id):   # 修改数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.update(request,id)

    def delete(self, request, id): # 删除数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.destroy(request,id)
"""

"""
# DRF 第六版 第三次次封装视图函数
from rest_framework.views import APIView
from rest_framework.response import Response
from SerDemo import serializers
from SerDemo import models


class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        '''

        :return:
        '''
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        '''

        :param args:
        :param kwargs:
        :return:
        '''
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):

    def list(self, request):
        queryset = self.get_queryset()
        ret = self.get_serializer(queryset, many=True)
        return Response(ret.data)


class CreateModelMixin(object):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ListCreateModelMixiin(GenericAPIView, ListModelMixin, CreateModelMixin):
    pass


class BookView(ListCreateModelMixiin):
    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request):  # 查看数据
        '''

        :param request:
        :return:
        '''
        return self.list(request)

    def post(self, request):  # 添加数据
        '''

        :param request:
        :return:
        '''
        return self.create(request)


class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        ret = self.get_serializer(book_obj)
        return Response(ret.data)


class UpdateModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)  # partial=True  允许部分更新
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DestroyModelMixin(object):

    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        book_obj.delete()
        return Response('delete')


class RetrieveUpdateDestroyAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass


class BookEditView(RetrieveUpdateDestroyAPIView):
    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request, id):  # 查看单条数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.retrieve(request, id)

    def put(self, request, id):  # 修改数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.update(request, id)

    def delete(self, request, id):  # 删除数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.destroy(request, id)


# class ViewSetMixin(object):
#     def as_view(self):
#         '''
#         按照我们参数指定的匹配
#         get --> list
#         :return:
#         '''
#         pass
from rest_framework.viewsets import ViewSetMixin # 框架自带

# 自己写的继承方法
class ModelViewSet(ViewSetMixin, GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass


# 案例
# get-->self.list
#
# class BookModeViewSet(ViewSetMixin, GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     query_set = models.Book.objects.all()
#     serializer_class = serializers.BookSerializer
#



class BookModeViewSet(ModelViewSet):
    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


"""

# """
# DRF 第七版 视图组件总结 优化
from rest_framework.views import APIView
from rest_framework.response import Response
from SerDemo import serializers
from SerDemo import models


class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        '''

        :return:
        '''
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        '''

        :param args:
        :param kwargs:
        :return:
        '''
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):

    def list(self, request):
        queryset = self.get_queryset()
        ret = self.get_serializer(queryset, many=True)
        return Response(ret.data)


class CreateModelMixin(object):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ListCreateModelMixiin(GenericAPIView, ListModelMixin, CreateModelMixin):
    pass


class BookView(ListCreateModelMixiin):
    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request):  # 查看数据
        '''

        :param request:
        :return:
        '''
        return self.list(request)

    def post(self, request):  # 添加数据
        '''

        :param request:
        :return:
        '''
        return self.create(request)


class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        ret = self.get_serializer(book_obj)
        return Response(ret.data)


class UpdateModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)  # partial=True  允许部分更新
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DestroyModelMixin(object):

    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(nid=id).first()
        book_obj.delete()
        return Response('delete')


class RetrieveUpdateDestroyAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass


class BookEditView(RetrieveUpdateDestroyAPIView):
    query_set = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get(self, request, id):  # 查看单条数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.retrieve(request, id)

    def put(self, request, id):  # 修改数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.update(request, id)

    def delete(self, request, id):  # 删除数据
        '''

        :param request:
        :param id:
        :return:
        '''
        return self.destroy(request, id)


from rest_framework.viewsets import ViewSetMixin # 框架自带


from rest_framework.viewsets import  ModelViewSet



class BookModeViewSet(ModelViewSet):
    queryset = models.Book.objects.all()  #query_set 使用框架自带的 queryset
    serializer_class = serializers.BookSerializer


from rest_framework import views  # 框架提供  --->  APIView(View):
from rest_framework import generics    #  ---> GenericAPIView(views.APIView):
from rest_framework import mixins      # --->
from rest_framework import viewsets
# """
