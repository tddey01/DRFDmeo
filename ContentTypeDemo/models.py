from django.db import models
from django.contrib.contenttypes.models import  ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.

class Food(models.Model):
    '''
    id  title
    1    面包
    2   牛奶
    '''
    id = models.AutoField(primary_key=True)
    # 不会生成字段 只用于反向查询
    title = models.CharField(max_length=32,verbose_name='类别')

    coupons = GenericRelation(to="Coupon",on_delete=None)


class Fruit(models.Model):
    '''
    id   title
    1   苹果
    2 香蕉
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name='种类')


# # 如果有40张表
# class Coupon(models.Model):
#     '''
#     id   title            food_id   frut_id
#     1    面包95折             1        null
#     2    香蕉满10元减五元       null     1
#     '''
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=32,verbose_name='打折')
#     fruit = models.ForeignKey(to='Fruit',to_field='id',on_delete=models.CASCADE)


# class Coupon(models.Model):
#     """
#     id      title        table_id      object_id
#     1       面包九五折       1             1
#     2       香蕉满10元减5元  2             2
#     """
#     title = models.CharField(max_length=32)
#     table = models.ForeignKey(to="Table")
#     object_id = models.IntegerField()
#
# class Table(models.Model):
#     '''
#     id      app_name        table_name
#     1       demo            food
#     2       demo            fruit
#     '''
#     app_name = models.CharField(max_length=32)
#     title = models.CharField(max_length=32)




class Coupon(models.Model):
    title = models.CharField(max_length=32)
    # 第一步
    content_type = models.ForeignKey(to=ContentType, on_delete=None)
    # 第二步
    object_id = models.IntegerField()
    # 第三步 不会生成字段
    content_object = GenericForeignKey("content_type", "object_id")
