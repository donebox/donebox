# -*- coding: utf-8 -*-

from django.urls import path

from .views import index

app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),
]
