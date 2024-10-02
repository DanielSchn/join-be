from django.db import models
from django.contrib.auth.models import User


# Create your models here.
    

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    letter = models.CharField(max_length=2)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Contacts'
    

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    assigned_to = models.ManyToManyField(User, related_name='tasks')
    due = models.DateField()
    prio = models.CharField(max_length=100, help_text="low, medium, urgent")
    category = models.IntegerField(help_text="1 = User Story, 2 = Technical Task")
    timestamp = models.BigIntegerField()
    status = models.CharField(max_length=100, default="toDo", help_text="toDo, inProgress, awaitingFeedback, done")
    subtasks = models.JSONField(default=list, null=True, blank=True, help_text="status: toDo, inProgress, awaitingFeedback, done")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Tasks'