# -*- coding: utf-8 -*-
from rest_framework import serializers

from btc_node.models import Wallet, BTCAccount


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'wallet', 'account_id', 'created')


class BTCAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTCAccount
        fields = ('id', 'name', 'is_default')
