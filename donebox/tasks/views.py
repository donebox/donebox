# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    task_form = TaskForm()

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'task_form': task_form
    })


def detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    return render(request, 'tasks/detail.html', {
        'task': task
    })


def register(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            task = task_form.save()

            return redirect('tasks:detail', task_id=task.id)
        else:
            task_form = TaskForm()

    return render(request, 'tasks/index.html', {
        'task_form': task_form
    })


def complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.complete()

    return redirect('tasks:detail', task_id=task.id)
