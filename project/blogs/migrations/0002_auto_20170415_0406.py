# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
