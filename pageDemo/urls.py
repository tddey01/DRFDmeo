#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.urls import path
from  pageDemo import views

urlpatterns = [
    path(r'book',views.BookView.as_view()),
    ]
