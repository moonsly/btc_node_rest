# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from btc_node.api import router
from btc_node.views import ProfileView


urlpatterns = [
    url(r'^accounts/login/?', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/?', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^profile/?', ProfileView.as_view(), name='profile'),
    url(r'^api/', include(router.urls)),
]
