# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.core.management import BaseCommand
from django.utils import timezone

from btc_node.models import BTCAccount, Wallet
from btc_node.utils import get_node_connect, get_wallets

logger = logging.getLogger('commands')


class Command(BaseCommand):
    help = """Удалить все Кошельки, запросить Кошельки от BTC ноды, заполнить в соответствии с Аккаунтом"""

    def handle(self, *args, **options):
        Wallet.objects.all().delete()

        conn = get_node_connect()
        accs = BTCAccount.objects.all()
        for acc in accs:
            print("Обрабатываем аккаунт {}".format(acc))
            wallets = get_wallets(conn, acc.name)
            for wallet in wallets:
                Wallet.objects.create(account=acc, wallet=wallet)
            print("Всего {} кошельков создано:\n{}".format(len(wallets), wallets))
