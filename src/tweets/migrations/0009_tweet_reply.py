# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0008_tweet_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='reply',
            field=models.BooleanField(default=False, verbose_name=b'Is a reply?'),
        ),
    ]
