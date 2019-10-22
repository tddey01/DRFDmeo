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
    "title": "alex全栈",
    "w_category": 1,
    "pub_time": "2019-10-19",
    "publish_nid": 1,
    "author_list": [1,2]
}

from SerDemo import models
class BookSerializer(serializers.Serializer):
    nid = serializers.IntegerField(required=False)  # required=False 不校验nid
    title = serializers.CharField(max_length=32)
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
    category = serializers.ChoiceField(choices=CHOICES, source='get_category_display',read_only=True) #read_only=True  序列化展示用
    w_category = serializers.ChoiceField(choices=CHOICES, write_only=True) # write_only 序列化
    pub_time = serializers.DateField()
    publish = PublisherSerializer(read_only=True)
    publish_nid = serializers.IntegerField(write_only=True) #
    author = AuthorSerializer(many=True,read_only=True)
    author_list = serializers.ListField(write_only=True) #



    def create(self,validated_data):  # {'nid': 1, 'title': 'python全栈', 'w_category': 1, 'pub_time': '2019-10-19', 'publish_nid': 1, 'author_list': [1]}
        book = models.Book.objects.create(title=validated_data['title'],category=validated_data['w_category'],pub_time=validated_data['pub_time'],
                                   publish_id=validated_data['publish_nid'])
        book.author.add(*validated_data['author_list'])
        return book
        
"""

"""
# 第四版 DRF

from rest_framework import serializers


class PublisherSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


book_obj = {
    "title": "alex全栈",
    "w_category": 1,
    "pub_time": "2019-10-19",
    "publish_nid": 1,
    "author_list": [1,2]
}

data = {
    "title": "Alex的使用教程2"
}

def my_validate(value):   # 自定义验证器  优先级高
    if "敏感信息" in value.lower():
        raise  serializers.ValidationError('不能含有敏感信息')
    else:
        return  value

from SerDemo import models
class BookSerializer(serializers.Serializer):
    nid = serializers.IntegerField(required=False)  # required=False 不校验nid
    title = serializers.CharField(max_length=32,validators=[my_validate])  # 列表 自定义验证
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))

    category = serializers.ChoiceField(choices=CHOICES, source='get_category_display',read_only=True) #read_only=True  序列化展示用
    w_category = serializers.ChoiceField(choices=CHOICES, write_only=True) # write_only 序列化

    pub_time = serializers.DateField()

    publish = PublisherSerializer(read_only=True)
    publish_nid = serializers.IntegerField(write_only=True) #

    author = AuthorSerializer(many=True,read_only=True)
    author_list = serializers.ListField(write_only=True) #



    def create(self,validated_data):  # {'nid': 1, 'title': 'python全栈', 'w_category': 1, 'pub_time': '2019-10-19', 'publish_nid': 1, 'author_list': [1]}
        book = models.Book.objects.create(title=validated_data['title'],category=validated_data['w_category'],pub_time=validated_data['pub_time'],
                                   publish_id=validated_data['publish_nid'])
        book.author.add(*validated_data['author_list'])
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.category = validated_data.get('category',instance.category)
        instance.pub_time = validated_data.get('pub_time',instance.pub_time)
        instance.publish_id = validated_data.get('publish_nid', instance.publish_id)
        if validated_data.get('author_list'):
            instance.author.set(validated_data['author_list'])
        instance.save()

        return  instance

    def validate_title(self,value):  # 验证  对单独字段进行校验
        if 'python' not in value.lower():
            raise  serializers.ValidationError('标题必须含有python')
        return  value

    def validate(self, attrs): # 全局验证钩子
        if attrs['w_category'] == 1 and attrs['publish_nid'] == 1:
            return attrs
        else:
            raise  serializers.ValidationError('分类以及标题不符合要求')
"""

"""
# 第五版
"""
from rest_framework import serializers
from SerDemo import models

class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


book_obj = {
        "title": "Alex的使用教程",
        "w_category": 1,
        "pub_time": "2018-10-09",
        "publisher_id": 1,
        "author_list": [1, 2]
    }


data = {
    "title": "Alex的使用教程2"
}


def my_validate(value):
    if "敏感信息" in value.lower():
        raise serializers.ValidationError("不能含有敏感信息")
    else:
        return value


class BookSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField(read_only=True)  # ModelSerializer 序列化过程

    def get_category_display(self,obj):
        return  obj.get_category_display()

    publish_info = serializers.SerializerMethodField(read_only=True)

    def get_publish_info(self,obj):
        # obj 序列化的每个book对象
        publish_obj = obj.publish
        return {'nid':publish_obj.id,'title':publish_obj.title}

    authors = serializers.SerializerMethodField(read_only=True)

    def get_authors(self,obj):
        author_query_set = obj.author.all()
        return [{'id':author_obj.id,'name':author_obj.name} for author_obj in author_query_set]


    class Meta:
        model = models.Book
        # fields = ['nid','title','pub_time']
        fields = '__all__' # 获取所有字段
        # depth = 1

        extra_kwargs = {
            "category":{
                "write_only":True
            },
            "publish":{
                "write_only": True
            },
            "author":{
                "write_only": True
            }
        }

