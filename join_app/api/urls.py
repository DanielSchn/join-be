from django.urls import path, include
from .views import ContactsView, TasksView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'contacts', ContactsView, basename='contacts')
router.register(r'tasks', TasksView, basename='tasks')


urlpatterns = [
    path('', include(router.urls)),
]