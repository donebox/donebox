# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404

from .models import Task


def index(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })


def detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    return render(request, 'tasks/detail.html', {
        'task': task
    })


def complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.is_completed = True
    task.save()

    return redirect('tasks:detail', task_id=task.id)
