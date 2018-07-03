DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btc_node',
        'USER': 'septemex',
        'PASSWORD': 'septemex',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CONSTANCE_CONFIG = {
    'NODE_LOGIN': ('cashberycoinrpc', 'node login'),
    'NODE_PASSWORD': ('3yXvc24JawmTncHduoA6er9MKWW7a4fu19NyRP1RtwPm', 'node password'),
    'NODE_IP': ('5.9.104.23', 'node IP'),
    'NODE_PORT': ('8332', 'node port'),
}
