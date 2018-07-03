# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from btc_node.views import ListWalletsView, ListAccountsView


router = DefaultRouter()

router.register('wallets', ListWalletsView)
router.register('accounts', ListAccountsView)
