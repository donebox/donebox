# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=140)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def complete(self):
        self.completed_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
