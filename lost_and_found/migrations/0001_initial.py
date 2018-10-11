# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='thing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thingname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50, null=True, verbose_name='\u8054\u7cfb\u65b9\u5f0f', blank=True)),
                ('state', models.CharField(blank=True, max_length=1, null=True, verbose_name='\u7269\u54c1\u72b6\u6001', choices=[(b'1', '\u5f04\u4e22\u7684\u5b9d\u8d1d'), (b'2', '\u6361\u5230\u7684\u5b9d\u8d1d')])),
                ('find_place', models.CharField(max_length=100)),
                ('find_date', models.DateField()),
                ('description', models.CharField(max_length=300, verbose_name='\u5b9d\u8d1d\u63cf\u8ff0')),
            ],
        ),
    ]
