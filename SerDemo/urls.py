#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.urls import path
from SerDemo import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"",views.BookModeViewSet)

urlpatterns = [
    # # # path('list/', views.BookView.as_view()),
    # # # path('retrieve/<int:id>', views.BookEditView.as_view()),  # 2.0 以前版本写法   2.0 以后版本写法 <init:id>
    # # path('list/', views.BookModeViewSet.as_view({"get": "list", "post": "create"})),
    # # path('retrieve/<int:id>', views.BookModeViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('list/', views.BookModeViewSet.as_view({"get": "list", "post": "create"})),
    path('retrieve/<int:pk>', views.BookModeViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]
# urlpatterns += router.urls # 自动生成路由 带参数     温馨提示 没有增删改查 不要使用自动生成路由
