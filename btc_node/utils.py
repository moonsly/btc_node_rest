# -*- coding: utf-8 -*-
import bitcoin
from constance import config

from btc_node.models import BTCAccount


def get_node_connect():
    """Получить коннект к ВТС ноде на основе constance.config"""
    login = config.NODE_LOGIN
    password = config.NODE_PASSWORD
    host = config.NODE_IP
    port = config.NODE_PORT
    conn = bitcoin.connect_to_remote(login, password, host, port)
    return conn


def get_default_account():
    """Получить аккаунт по умолчанию из БД"""
    accs = BTCAccount.objects.filter(is_default=True)
    if accs:
        return accs.first().name
    else:
        return None


def get_wallets(conn, account):
    """Вернуть все кошельки с ВТС ноды по аккаунту"""
    return conn.getaddressesbyaccount(account)


def get_balance(conn):
    """Баланс ноды"""
    return conn.getbalance()


def create_wallet(conn, account):
    """Создать новый кошелек на BTC ноде/аккаунте"""
    addr2 = conn.getnewaddress(account)
    return addr2
