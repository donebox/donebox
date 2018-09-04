# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import Task


def index(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })


def detail(request, task_id):
    task = Task.objects.get(id=task_id)

    return render(request, 'tasks/detail.html', {
        'task': task
    })
