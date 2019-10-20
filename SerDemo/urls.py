#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.urls import path
from django.urls import include

from .views import BookView
urlpatterns = [
    path('list/', BookView.as_view()),
]

