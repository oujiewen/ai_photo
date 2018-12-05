#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    name=models.CharField(max_length=100) #发布会名称
    limit=models.IntegerField() #参加人数
    status=models.IntegerField() #状态
    address=models.CharField(max_length=200) #地址
    start_time=models.DateField('events time') #发布会时间
    create_time=models.DateField(auto_now=True) #创建时间

    def __unicode__(self):
        return self.name

class Guest(models.Model):
    event=models.ForeignKey(Event) #关联发布会id
    realname=models.CharField(max_length=64)
    phone=models.CharField(max_length=16)
    email=models.EmailField()
    sign=models.BooleanField()
    create_time=models.DateTimeField(auto_now=True) #创建时间

    class Meta:
        unique_together=("event","phone")

    def __unicode__(self):
        return self.realname