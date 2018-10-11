# -*- coding: utf-8 -*-
from django.db import models


class thing(models.Model):
    thingname= models.CharField(max_length=100)
 #   announcer  = models.ForeignKey(User, verbose_name=u'提出人', null=False, blank=False)
    contact = models.CharField(u'联系方式', max_length=50, null=True, blank=True)
    STATUS_CHOICES = (('1', u'弄丢的宝贝'), ('2', u'捡到的宝贝'))
    state = models.CharField(u'物品状态', max_length=1, null=True, blank=True, choices=STATUS_CHOICES)
    find_place = models.CharField(max_length=100)
    find_date = models.DateField()
    description = models.CharField(u'宝贝描述',max_length=300, null=False, blank=False)


    def __unicode__(self):
        return self

class User(models.Model):
    name = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    contaction  = models.CharField(max_length=100)
    #RANGE_CHOICES = (('1', u'有心路人'), ('2', u'善良天使'),('3', u'热情雷锋'))
    #range = state = models.CharField(u'用户等级', max_length=1, null=True, blank=True, choices=RANGE_CHOICES)


