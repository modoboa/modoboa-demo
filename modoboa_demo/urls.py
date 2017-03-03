# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sendvirus/$', views.send_virus, name="virus_send"),
    url(r'^sendspam/$', views.send_spam, name="spam_send"),
]
