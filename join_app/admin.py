from django.contrib import admin
from .models import Tasks, Users, Contacts


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


# Register your models here.
admin.site.register(Contacts, ContactAdmin)
admin.site.register(Users, UserAdmin)
admin.site.register(Tasks, TaskAdmin)