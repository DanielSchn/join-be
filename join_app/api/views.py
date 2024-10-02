from rest_framework import viewsets
from .serializers import ContactsSerializer, TasksSerializer
from join_app.models import Contacts, Tasks
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TasksView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]