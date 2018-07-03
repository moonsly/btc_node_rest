# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import list_route
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from constance import config

from btc_node.models import BTCAccount, Wallet
from btc_node.serializers import WalletSerializer,BTCAccountSerializer
from btc_node.utils import (get_node_connect, get_balance, get_wallets,
                            create_wallet, get_default_account)


class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


class ListWalletsView(ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WalletSerializer
    queryset = Wallet.objects.filter(account__name=get_default_account())

    def get_queryset(self):
        if self.request.GET.get("account"):
            return Wallet.objects.filter(account__name=self.request.GET.get("account"))

        else:
            return Wallet.objects.filter(account__name=get_default_account())

    def create(self, request):
        """POST методы - проверить баланс, создать BTC кошелек на ноде"""
        method = request.data.get("method")
        if method and method == "create_wallet":
            conn = get_node_connect()

            account = self.request.data.get("account") or get_default_account()

            acc_obj = BTCAccount.objects.filter(name=account).first()
            if not acc_obj:
                raise ValidationError("Incorrect account name {}".format(account))

            new_wallet = create_wallet(conn, account)
            Wallet.objects.create(account=acc_obj, wallet=new_wallet)

            return Response({"wallet_created": new_wallet, "account": account})

        return Response({"method": method, "available_methods": ["create_wallet"]})



class ListAccountsView(ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BTCAccountSerializer
    queryset = BTCAccount.objects.all()

    @list_route()
    def default(self, request, *args, **kwargs):
        """ Вернуть accоunt по умолчанию """
        account = get_default_account()
        return Response({"default_account": account})

    @list_route()
    def params(self, request, *args, **kwargs):
        """ Вернуть настройки json RPC для ноды """
        params = ("login", "password", "IP", "port")
        res = []
        for param in params:
            res.append({"key": param, "value": getattr(config, "NODE_{}".format(param.upper()))})
        res.append({"key": "default_account", "value": get_default_account()})

        return Response({"settings": res})

    @list_route()
    def balance(self, request, *args, **kwargs):
        """ Balance """
        conn = get_node_connect()
        balance = get_balance(conn)
        return Response({"balance": balance})
