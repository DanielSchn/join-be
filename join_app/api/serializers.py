from rest_framework import serializers
from join_app.models import Contacts, Tasks


class ContactsSerializer(serializers.ModelSerializer):
    """
    Serializer für Kontakte.

    Dieser Serializer konvertiert die 'Contacts'-Daten zwischen Python-Objekten
    und JSON. Er ermöglicht die Erstellung, Aktualisierung und Validierung von
    Kontaktinformationen.

    Felder:
    - Alle Felder des 'Contacts' Modells werden unterstützt, da 'fields' auf
      '__all__' gesetzt ist.

    Nutzung:
    - Wird verwendet, um Kontaktinformationen in API-Anfragen und -Antworten zu verarbeiten.
    """
    class Meta:
        model = Contacts
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    """
    Serializer für Aufgaben.

    Dieser Serializer konvertiert die 'Tasks'-Daten zwischen Python-Objekten
    und JSON. Er ermöglicht die Erstellung, Aktualisierung und Validierung von
    Aufgabeninformationen.

    Felder:
    - Alle Felder des 'Tasks' Modells werden unterstützt, da 'fields' auf
      '__all__' gesetzt ist.

    Nutzung:
    - Wird verwendet, um Aufgabeninformationen in API-Anfragen und -Antworten zu verarbeiten.
    """
    class Meta:
        model = Tasks
        fields = '__all__'