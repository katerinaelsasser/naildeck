# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-30 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200730_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=6),
        ),
    ]
