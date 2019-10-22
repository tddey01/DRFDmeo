#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from django.urls import path
from parserDemo import views


urlpatterns = [
    path('demo', views.DjangoView.as_view()),
    path('test', views.DRFView.as_view()),


]