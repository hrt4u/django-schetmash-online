# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinekassa', '0003_receipt_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
