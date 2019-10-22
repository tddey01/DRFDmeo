import  uuid
from  authDemo import models
from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import   Response

# Create your views here.

class Demoview(APIView):

    def  get(self,request):
        return Response('认证demo~..')

class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        pwd = request.data.get('pwd')
        token = uuid.uuid4()
        models.User.objects.create(username=username,pwd=pwd,token=token)
        return  Response('创建成功')

class TestView(APIView):

    def get(self,request):
        return  Response("认证测试")