# coding: utf-8
from django.urls import path

from . import views

app_name = 'modoboa_demo'

urlpatterns = [
    path('sendvirus/', views.send_virus, name="virus_send"),
    path('sendspam/', views.send_spam, name="spam_send"),
]
