#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

'''
# DRF 第一版
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    title = serializers.CharField(max_length=32)
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
    category = serializers.ChoiceField(choices=CHOICES, source='get_category_display')
    pub_time = serializers.DateField()
'''

"""
# 第二版 DRF

from rest_framework import serializers


class PublisherSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    name = serializers.CharField(max_length=32)

class BookSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    title = serializers.CharField(max_length=32)
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
    category = serializers.ChoiceField(choices=CHOICES, source='get_category_display')
    pub_time = serializers.DateField()
    publish = PublisherSerializer()
    author = AuthorSerializer(many=True)
    
"""

# 第三版 DRF

from rest_framework import serializers


class PublisherSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


book_obj = {
    "nid": 1,
    "title": "python全栈",
    "w_category": 1,
    "pub_time": "2019-10-19",
    "publish_nid": 1,
    "author_list": [1]
}


class BookSerializer(serializers.Serializer):
    nid = serializers.IntegerField(required=False)  # required=False 不校验nid
    title = serializers.CharField(max_length=32)
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
    category = serializers.ChoiceField(choices=CHOICES, source='get_category_display',read_only=True) #read_only=True  序列化展示用
    w_category = serializers.ChoiceField(choices=CHOICES, read_only=True) #read_only=True  反序列化展示用  前端传入数据
    pub_time = serializers.DateField()
    publish = PublisherSerializer(read_only=True)
    publish_nid = serializers.IntegerField(write_only=True) #
    author = AuthorSerializer(many=True,read_only=True)
    author_list = serializers.ListField(write_only=True) #