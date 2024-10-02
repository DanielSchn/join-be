from rest_framework import mixins, viewsets
from .serializers import UsersSerializer, ContactsSerializer, TasksSerializer
from join_app.models import Contacts, Tasks, Users
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class TasksView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]