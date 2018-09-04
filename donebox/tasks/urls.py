# -*- coding: utf-8 -*-

from django.urls import path

from .views import index, detail

app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),
    path('<int:task_id>/', detail, name='detail'),
]
