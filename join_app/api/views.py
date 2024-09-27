from rest_framework import mixins, viewsets
from .serializers import UsersSerializer, ContactsSerializer, TasksSerializer
from join_app.models import Users, Contacts, Tasks


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class TasksView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer