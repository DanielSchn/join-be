from django.contrib import admin
from .models import Tasks, Users, Contacts
from django.utils import timezone
from django import forms


class TaskAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskAdminForm, self).__init__(*args, **kwargs)
        self.fields['due'].initial = timezone.now().date()
        self.fields['timestamp'].initial = int(timezone.now().timestamp())
        self.fields['subtasks'].initial = [{"title": "", "status": "toDo"}]
        self.fields['prio'].initial = 'low'
        self.fields['status'].initial = 'toDo'
        self.fields['category'].initial = '1'


class UserAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name', 'email']
    exclude = ['password']

class ContactAdmin(admin.ModelAdmin):
    list_filter = ['name', 'letter']
    list_display = ['name', 'mail', 'letter', 'number']


class TaskAdmin(admin.ModelAdmin):
    list_filter = ['title', 'assigned_to', 'prio', 'due']
    list_display = ['title', 'due', 'prio', 'category', 'status']
    form = TaskAdminForm


# Register your models here.
admin.site.register(Contacts, ContactAdmin)
admin.site.register(Users, UserAdmin)
admin.site.register(Tasks, TaskAdmin)