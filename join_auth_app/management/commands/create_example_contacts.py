from django.core.management.base import BaseCommand
from join_app.api.serializers import ContactsSerializer


class Command(BaseCommand):
    help = 'Erstellt Beispielkontakte!'

    def handle(self, *args, **kwargs):
        """
        Führt den Command aus, um Beispielkontakte zu erstellen.
        """
        contacts_data = [
            {
                'name': 'Anna Müller',
                'mail': 'anna.mueller@example.com',
                'number': '+491512345678',
                'letter': 'A',
                'color': '#FF5733',
            },
            {
                'name': 'Ben Schneider',
                'mail': 'ben.schneider@example.com',
                'number': '+491512345679',
                'letter': 'B',
                'color': '#33FF57',
            },
            {
                'name': 'Clara Schulz',
                'mail': 'clara.schulz@example.com',
                'number': '+491512345680',
                'letter': 'C',
                'color': '#3357FF',
            },
            {
                'name': 'David Fischer',
                'mail': 'david.fischer@example.com',
                'number': '+491512345681',
                'letter': 'D',
                'color': '#FF33A1',
            },
            {
                'name': 'Ella Becker',
                'mail': 'ella.becker@example.com',
                'number': '+491512345682',
                'letter': 'E',
                'color': '#A133FF',
            },
            {
                'name': 'Eric Hoffmann',
                'mail': 'eric.hoffmann@example.com',
                'number': '+491512345683',
                'letter': 'E',
                'color': '#FFAA33',
            },
            {
                'name': 'Greta Weber',
                'mail': 'greta.weber@example.com',
                'number': '+491512345684',
                'letter': 'G',
                'color': '#33FFAA',
            },
            {
                'name': 'Henry König',
                'mail': 'henry.koenig@example.com',
                'number': '+491512345685',
                'letter': 'H',
                'color': '#AA33FF',
            },
            {
                'name': 'Isabella Wolf',
                'mail': 'isabella.wolf@example.com',
                'number': '+491512345686',
                'letter': 'I',
                'color': '#33AAFF',
            },
            {
                'name': 'Jonas Krause',
                'mail': 'jonas.krause@example.com',
                'number': '+491512345687',
                'letter': 'J',
                'color': '#FF33AA',
            },
        ]

        for contact_data in contacts_data:
            serializer = ContactsSerializer(data=contact_data)
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(f"Kontakt {contact_data['name']} wurde erstellt."))
            else:
                self.stderr.write(self.style.ERROR(f"Fehler beim Erstellen von Kontakt {contact_data['name']}: {serializer.errors}"))
