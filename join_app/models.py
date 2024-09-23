from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    initials = models.CharField(max_length=2)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'User'
    

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
        verbose_name_plural = 'Contact'
    

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    assigned_to = models.ManyToManyField(Users, related_name='tasks')
    due = models.DateField()
    prio = models.CharField(max_length=100)
    category = models.IntegerField()
    timestamp = models.BigIntegerField()
    status = models.CharField(max_length=100, default="toDo")
    subtasks = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Task'