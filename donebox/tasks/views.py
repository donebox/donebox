# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.urls import reverse
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


def complete(request, task_id):
    task = Task.objects.get(id=task_id)

    task.is_completed = True
    task.save()

    return HttpResponseRedirect(
        reverse('tasks:detail', args=(task.id,)))
