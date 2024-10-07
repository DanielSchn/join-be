from django.db import models
from django.contrib.auth.models import User


# Create your models here.
    

class Contacts(models.Model):
    """
    Modell für Kontakte.

    Dieses Modell speichert Kontaktinformationen für Benutzer.
    Es enthält die folgenden Felder:

    - **name**: Der Name des Kontakts (string, max. 100 Zeichen).
    - **mail**: Die E-Mail-Adresse des Kontakts (string, max. 100 Zeichen).
    - **number**: Die Telefonnummer des Kontakts (string, max. 100 Zeichen).
    - **letter**: Eine zwei Zeichen lange Abkürzung oder Kennung für den Kontakt (string, max. 2 Zeichen).
    - **color**: Eine bevorzugte Farbe für den Kontakt (string, max. 10 Zeichen).

    Methoden:
    - **__str__()**: Gibt den Namen des Kontakts als lesbare Darstellung zurück.

    Meta-Optionen:
    - **ordering**: Kontakte werden standardmäßig nach Namen sortiert.
    - **verbose_name_plural**: Der Name für die Pluralform im Admin-Bereich.
    """
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    letter = models.CharField(max_length=2)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Contacts'
    

class Tasks(models.Model):
    """
    Modell für Aufgaben.

    Dieses Modell speichert Aufgabeninformationen und verknüpft sie mit Benutzern.
    Es enthält die folgenden Felder:

    - **title**: Der Titel der Aufgabe (string, max. 100 Zeichen).
    - **description**: Eine detaillierte Beschreibung der Aufgabe (string, max. 500 Zeichen).
    - **assigned_to**: Ein ManyToMany-Feld, das angibt, welche Benutzer der Aufgabe zugewiesen sind.
    - **due**: Das Fälligkeitsdatum der Aufgabe (Datum).
    - **prio**: Die Priorität der Aufgabe (string, max. 100 Zeichen; mögliche Werte: "low", "medium", "urgent").
    - **category**: Eine ganze Zahl zur Kategorisierung der Aufgabe (integer; 1 = User Story, 2 = Technical Task).
    - **timestamp**: Ein Zeitstempel für die Erstellung oder Aktualisierung der Aufgabe (BigInteger).
    - **status**: Der Status der Aufgabe (string, max. 100 Zeichen; Standardwert: "toDo", mögliche Werte: "toDo", "inProgress", "awaitingFeedback", "done").
    - **subtasks**: Eine JSONField, die eine Liste von Unteraufgaben speichert (standardmäßig eine leere Liste).

    Methoden:
    - **__str__()**: Gibt den Titel der Aufgabe als lesbare Darstellung zurück.

    Meta-Optionen:
    - **ordering**: Aufgaben werden standardmäßig nach Titel sortiert.
    - **verbose_name_plural**: Der Name für die Pluralform im Admin-Bereich.
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    assigned_to = models.ManyToManyField(User, related_name='tasks')
    due = models.DateField()
    prio = models.CharField(max_length=100, help_text="low, medium, urgent")
    category = models.IntegerField(help_text="1 = User Story, 2 = Technical Task")
    timestamp = models.BigIntegerField()
    status = models.CharField(max_length=100, default="toDo", help_text="toDo, inProgress, awaitingFeedback, done")
    subtasks = models.JSONField(default=list, null=True, blank=True, help_text="status: toDo, inProgress, awaitingFeedback, done")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Tasks'