from django.urls import path, include
from .views import UsersView, ContactsView, TasksView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UsersView, basename='users')
router.register(r'contacts', ContactsView, basename='contacts')
router.register(r'tasks', TasksView, basename='tasks')


urlpatterns = [
    path('', include(router.urls)),
    # path('users/', UsersView.as_view({'get': 'list'}), name='users'),
    # path('contacts/', ContactsView.as_view({'get': 'list'}), name='contacts'),
    # path('tasks/', TasksView.as_view({'get': 'list'}), name='tasks'),
]