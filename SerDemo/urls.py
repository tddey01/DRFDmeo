#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.urls import path
from SerDemo import views

urlpatterns = [
    # path('list/', views.BookView.as_view()),
    # path('retrieve/<int:id>', views.BookEditView.as_view()),  # 2.0 以前版本写法   2.0 以后版本写法 <init:id>
    path('list/', views.BookModeViewSet.as_view({"get": "list", "post": "create"})),
    path('retrieve/<int:id>', views.BookModeViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]

