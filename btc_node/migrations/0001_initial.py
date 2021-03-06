# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-03 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BTCAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0410\u043a\u043a\u0430\u0443\u043d\u0442 \u043d\u0430 BTC \u043d\u043e\u0434\u0435')),
                ('is_default', models.BooleanField(default=False, verbose_name='\u0410\u043a\u043a\u0430\u0443\u043d\u0442 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0410\u043a\u043a\u0430\u0443\u043d\u0442 \u043d\u0430 BTC \u043d\u043e\u0434\u0435')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btc_node.BTCAccount')),
            ],
        ),
    ]
