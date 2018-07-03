# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BTCAccount(models.Model):
    """Аккаунты на BTC ноде"""
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Аккаунт на BTC ноде')
    is_default = models.BooleanField(default=False, verbose_name='Аккаунт по умолчанию')

    def __unicode__(self):
        return "{}: {}".format(self.pk, self.name)


class Wallet(models.Model):
    """Кошельки на BTC ноде"""
    wallet = models.CharField(max_length=100, null=True, blank=True, verbose_name='Кошелек на BTC ноде')
    account = models.ForeignKey(BTCAccount, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
