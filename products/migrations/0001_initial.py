# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-30 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.CharField(choices=[('Polishes', 'Polishes'), ('Care', 'Care')], default='Polishes', max_length=15)),
            ],
        ),
    ]
