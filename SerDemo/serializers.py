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

'''
# 第二版 DRF
'''
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
    publish =PublisherSerializer()
    author = AuthorSerializer(many=True)
