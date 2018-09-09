# -*- coding: utf-8 -*-

from django.urls import path

from .views import index, detail, register, complete

app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('<int:task_id>/', detail, name='detail'),
    path('<int:task_id>/complete/', complete, name='complete'),
]
