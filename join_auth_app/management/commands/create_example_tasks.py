from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from join_app.api.serializers import TasksSerializer
from datetime import datetime, timedelta


from join_app.models import Tasks


class Command(BaseCommand):
    help = 'Erstellt Beispieltasks incl. Subtasks!'

    def handle(self, *args, **kwargs):
        """
        Führt den Command aus, um Beispieltasks zu erstellen.
        """
        today = datetime.today()

        tasks_data = [
            {
                'title': 'Entwicklung einer neuen Website',
                'description': 'Erstellung einer neuen Website für ein Unternehmen',
                'assigned_to': [
                    User.objects.get(username='alice_white').id,
                    User.objects.get(username='charlie_black').id,
                    User.objects.get(username='guest').id
                ],
                'due': (today + timedelta(days=25)).strftime('%Y-%m-%d'),
                'prio': 'medium',
                'category': 1,
                'timestamp': 1643723400,
                'status': 'toDo',
                'subtasks': [
                    {'title': 'Erstellung des Designs', 'status': 'toDo'}
                ]
            },
            {
                'title': 'Implementierung einer neuen Funktion',
                'description': 'Implementierung einer neuen Funktion in einer bestehenden Anwendung',
                'assigned_to': [
                    User.objects.get(username='bob_brown').id,
                    User.objects.get(username='alice_white').id,
                    User.objects.get(username='charlie_black').id,
                ],
                'due': (today + timedelta(days=10)).strftime('%Y-%m-%d'),
                'prio': 'urgent',
                'category': 0,
                'timestamp': 1643723400,
                'status': 'inProgress',
                'subtasks': [
                    {'title': 'Erstellung des Designs', 'status': 'done'},
                    {'title': 'Implementierung der Funktion', 'status': 'toDo'}
                ]
            },
            {
                'title': 'Überprüfung der Sicherheit',
                'description': 'Überprüfung der Sicherheit einer Anwendung',
                'assigned_to': [
                    User.objects.get(username='john_doe').id,
                    User.objects.get(username='jane_smith').id,
                    User.objects.get(username='bob_brown').id,
                ],
                'due': (today + timedelta(days=5)).strftime('%Y-%m-%d'),
                'prio': 'low',
                'category': 0,
                'timestamp': 1643723400,
                'status': 'awaitFeedback',
                'subtasks': []
            },
            {
                'title': 'Entwicklung einer neuen Anwendung',
                'description': 'Entwicklung einer neuen Anwendung für ein Unternehmen',
                'assigned_to': [
                    User.objects.get(username='bob_brown').id,
                    User.objects.get(username='alice_white').id,
                    User.objects.get(username='charlie_black').id,
                ],
                'due': (today + timedelta(days=25)).strftime('%Y-%m-%d'),
                'prio': 'medium',
                'category': 1,
                'timestamp': 1643723400,
                'status': 'toDo',
                'subtasks': [
                    {'title': 'Erstellung des Designs', 'status': 'toDo'},
                    {'title': 'Implementierung der Funktion', 'status': 'toDo'},
                    {'title': 'Testen der Anwendung', 'status': 'toDo'}
                ]
            },
            {
                'title': 'Überprüfung der Leistung',
                'description': 'Überprüfung der Leistung einer Anwendung',
                'assigned_to': [
                    User.objects.get(username='john_doe').id,
                    User.objects.get(username='jane_smith').id,
                    User.objects.get(username='bob_brown').id,
                    User.objects.get(username='alice_white').id,
                ],
                'due': (today + timedelta(days=1)).strftime('%Y-%m-%d'),
                'prio': 'low',
                'category': 0,
                'timestamp': 1643723400,
                'status': 'done',
                'subtasks': []
            },
            {
                'title': 'Implementierung einer neuen Funktion',
                'description': 'Implementierung einer neuen Funktion in einer bestehenden Anwendung',
                'assigned_to': [
                    User.objects.get(username='john_doe').id,
                    User.objects.get(username='jane_smith').id,
                    User.objects.get(username='bob_brown').id,
                    User.objects.get(username='alice_white').id,
                    User.objects.get(username='guest').id
                ],
                'due': (today + timedelta(days=9)).strftime('%Y-%m-%d'),
                'prio': 'urgent',
                'category': 0,
                'timestamp': 1643723400,
                'status': 'inProgress',
                'subtasks': [
                    {'title': 'Erstellung des Designs', 'status': 'done'},
                    {'title': 'Implementierung der Funktion', 'status': 'inProgress'}
                ]
            },
        ]

        for task_data in tasks_data:
            serializer = TasksSerializer(data=task_data)
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    f"Task {task_data['title']} wurde erstellt."))
            else:
                self.stdout.write(self.style.ERROR(
                    f"Task {task_data['title']} konnte nicht erstellt werden."))
