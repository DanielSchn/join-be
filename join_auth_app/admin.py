from django.contrib import admin
from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_filter = ['initials']
    list_display = ['user', 'initials', 'color']


# Register your models here.
admin.site.register(UserProfile, UserAdmin)