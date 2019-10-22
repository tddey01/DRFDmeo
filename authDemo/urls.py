#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from django.urls import path
from authDemo import views
urlpatterns = [
    path(r'',views.Demoview.as_view()),
    path(r'login/',views.LoginView.as_view()),
]
