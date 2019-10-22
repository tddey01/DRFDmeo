import  uuid
from  authDemo import models
from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import   Response
from  utils import auth
from utils import permission
from utils import  throttle

# Create your views here.

class Demoview(APIView):

    def  get(self,request):
        return Response('认证demo~..')

class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        pwd = request.data.get('pwd')
        # 登录成功 生成token 会把token给返回
        token = uuid.uuid4()
        models.User.objects.create(username=username,pwd=pwd,token=token)
        return  Response('创建成功')

class TestView(APIView):
    authentication_classes = [auth.MyAuth] # 局部视图
    permission_classes = [permission.MyPermission] #权限类
    throttle_classes = [throttle.MyThrottle, ]

    def get(self,request):
        print(request.user)
        print(request.auth)
        # user_obj = object.user.id
        return  Response("认证测试")