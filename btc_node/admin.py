# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from btc_node.models import BTCAccount, Wallet

class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    list_display = ('id', 'wallet', 'account', 'created')
    list_filter = ('account',)


admin.site.register(BTCAccount)
admin.site.register(Wallet, WalletAdmin)
