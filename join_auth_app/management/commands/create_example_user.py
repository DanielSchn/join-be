from django.core.management.base import BaseCommand
from join_auth_app.api.serializers import RegistrationSerializer


class Command(BaseCommand):
    help = 'Erstellt Beispielbenutzer!'

    def handle(self, *args, **kwargs):
        """
        Führt den Command aus, um den Beispielbenutzer zu erstellen.
        """
        users_data = [
            {
                'username': 'john_doe',
                'email': 'john.doe@example.com',
                'password': 'password123',
                'repeated_password': 'password123',
                'initials': 'JD',
                'color': '#FF0000',
                'first_name': 'John',
                'last_name': 'Doe',
            },
            {
                'username': 'jane_smith',
                'email': 'jane.smith@example.com',
                'password': 'securepass',
                'repeated_password': 'securepass',
                'initials': 'JS',
                'color': '#00FF00',
                'first_name': 'Jane',
                'last_name': 'Smith',
            },
            {
                'username': 'bob_brown',
                'email': 'bob.brown@example.com',
                'password': 'mypassword',
                'repeated_password': 'mypassword',
                'initials': 'BB',
                'color': '#0000FF',
                'first_name': 'Bob',
                'last_name': 'Brown',
            },
            {
                'username': 'alice_white',
                'email': 'alice.white@example.com',
                'password': 'alicepass',
                'repeated_password': 'alicepass',
                'initials': 'AW',
                'color': '#FFFF00',
                'first_name': 'Alice',
                'last_name': 'White',
            },
            {
                'username': 'charlie_black',
                'email': 'charlie.black@example.com',
                'password': 'charlie123',
                'repeated_password': 'charlie123',
                'initials': 'CB',
                'color': '#800080',
                'first_name': 'Charlie',
                'last_name': 'Black',
            },
        ]

        for user_data in users_data:
            serializer = RegistrationSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(f"Benutzer {user_data['username']} wurde erstellt."))
            else:
                self.stderr.write(self.style.ERROR(f"Fehler beim Erstellen von Benutzer {user_data['username']}: {serializer.errors}"))
