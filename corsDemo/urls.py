#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-


from django.urls import path
from corsDemo import views

urlpatterns = [
    path('demo/', views.DemoView.as_view()),
]
