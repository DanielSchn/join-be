from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """
        Hier werden alle Commands gebündelt aufgerufen um alle Beispieldaten usw. zu generieren.
        1. Datenbank wird geleert.
        2. Beispielbenutzer werden erstellt.
        3. Gastbenutzer wird erstellt.
        4. Beispielkontakte werden erstellt.
        5. Beispieltasks werden erstellt.
        """
        commands = [
            ('flush', {'interactive': False}),
            'create_example_user',
            'create_guest_user',
            'create_example_contacts',
            'create_example_tasks',
        ]

        for command in commands:
            if isinstance(command, tuple):
                command_name, options = command
                self.stdout.write(self.style.WARNING(f"Ausführen von {command_name}..."))
                call_command(command_name, **options)
            else:
                self.stdout.write(self.style.WARNING(f"Ausführen von {command}..."))
                call_command(command)
            self.stdout.write(self.style.SUCCESS(f"{command} erfolgreich ausgeführt."))
