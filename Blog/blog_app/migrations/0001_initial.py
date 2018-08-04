# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='博客标题')),
                ('category', models.CharField(blank=True, max_length=50, verbose_name='博客标签')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ['-pub_date'],
                'verbose_name': '文章',
            },
        ),
    ]
