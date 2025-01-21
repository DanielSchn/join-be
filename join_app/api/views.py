from rest_framework import viewsets
from .serializers import ContactsSerializer, TasksSerializer
from join_app.models import Contacts, Tasks
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ContactsView(viewsets.ModelViewSet):
    """
    API-ViewSet für Kontakte.

    Dieses ViewSet ermöglicht die Verwaltung von Kontaktinformationen. 
    Es unterstützt die folgenden HTTP-Methoden:

    - **GET**: Gibt eine Liste aller Kontakte oder einen bestimmten Kontakt zurück.
    - **POST**: Erstellt einen neuen Kontakt.
    - **PUT/PATCH**: Aktualisiert einen bestehenden Kontakt.
    - **DELETE**: Löscht einen bestehenden Kontakt.

    Berechtigungen:
    - **IsAuthenticatedOrReadOnly**: Authentifizierte Benutzer können Kontakte erstellen, aktualisieren und löschen.
    - Nicht authentifizierte Benutzer haben nur Lesezugriff.

    Nutzung:
    - Dieses ViewSet verwendet das 'Contacts' Modell und den 'ContactsSerializer'.
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]


class TasksView(viewsets.ModelViewSet):
    """
    API-ViewSet für Aufgaben.

    Dieses ViewSet ermöglicht die Verwaltung von Aufgaben.
    Es unterstützt die folgenden HTTP-Methoden:

    - **GET**: Gibt eine Liste aller Aufgaben oder eine bestimmte Aufgabe zurück.
    - **POST**: Erstellt eine neue Aufgabe.
    - **PUT/PATCH**: Aktualisiert eine bestehende Aufgabe.
    - **DELETE**: Löscht eine bestehende Aufgabe.

    Berechtigungen:
    - **IsAuthenticatedOrReadOnly**: Authentifizierte Benutzer können Aufgaben erstellen, aktualisieren und löschen.
    - Nicht authentifizierte Benutzer haben nur Lesezugriff.

    Nutzung:
    - Dieses ViewSet verwendet das 'Tasks' Modell und den 'TasksSerializer'.
    """
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]