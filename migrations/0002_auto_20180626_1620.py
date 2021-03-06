# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinekassa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='error_message',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Сообщение об ошибке'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='fns_site',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='status',
            field=models.CharField(choices=[('new', 'новый'), ('processing', 'в процессе'), ('success', 'успешно'), ('error', 'ошибка')], default='new', max_length=16, verbose_name='Статус чека'),
        ),
    ]
