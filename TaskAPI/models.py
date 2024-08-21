from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from base.model import BaseModel 

class STATUS_CHOICES(models.TextChoices):
    """
    types of status from task
    """
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'

class PRIORITY_CHOICES(models.TextChoices):
    """
    types of priority from task
    """
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class Task(BaseModel):


    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default=STATUS_CHOICES.TO_DO)
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES.LOW)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class TaskAssignment(BaseModel):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

class Comment(BaseModel):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
