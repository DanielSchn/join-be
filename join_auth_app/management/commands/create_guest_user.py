from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from join_auth_app.models import UserProfile

class Command(BaseCommand):
    help = 'Erstellt einen Gastnutzer mit einem zugehörigen UserProfile.'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='guest').exists():
            account = User.objects.create_user(
                username='guest',
                email='guest@guest.de',
                password='guest'
            )
            account.first_name = 'Guest'
            account.last_name = 'User'
            account.save()

            initials = 'GU'
            color = '#DC3DF5'
            UserProfile.objects.create(user=account, initials=initials, color=color)

            self.stdout.write(self.style.SUCCESS('Gastbenutzer wurde erfolgreich erstellt.'))
        else:
            self.stdout.write(self.style.WARNING('Gastbenutzer existiert bereits.'))
