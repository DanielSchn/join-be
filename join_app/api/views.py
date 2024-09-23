from rest_framework import mixins, viewsets
from .serializers import UsersSerializer, ContactsSerializer, TasksSerializer
from join_app.models import Users, Contacts, Tasks


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CreateListUpdateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    pass


class ContactsView(CreateListUpdateDestroyViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class TasksView(CreateListUpdateDestroyViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer