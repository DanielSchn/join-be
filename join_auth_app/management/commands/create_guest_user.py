from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from join_auth_app.models import UserProfile

class Command(BaseCommand):
    """
    Dieses Management Command erstellt einen Gastbenutzer mit einem zugehörigen UserProfile.
    
    Es überprüft zuerst, ob ein Benutzer mit dem Benutzernamen 'guest' bereits existiert. 
    Falls nicht, wird der Benutzer mit voreingestellten Werten (Benutzername, E-Mail und Passwort) 
    sowie einem zugehörigen Profil (Initialen und Farbe) angelegt.
    """
    help = 'Erstellt einen Gastnutzer mit einem zugehörigen UserProfile.'

    def handle(self, *args, **kwargs):
        """
        Führt den Command aus, um den Gastbenutzer und das UserProfile zu erstellen.
        
        Überprüft, ob der Benutzer mit dem Benutzernamen 'guest' existiert.
        Falls nicht, wird der Benutzer erstellt, und ein zugehöriges UserProfile angelegt.
        Gibt nach erfolgreicher Erstellung eine Bestätigungsmeldung aus oder eine Warnmeldung,
        wenn der Benutzer bereits existiert.

        Returns:
            Gibt eine Statusmeldung über die Konsole aus.
        """
        if not User.objects.filter(username='guest').exists():
            account = User.objects.create_user(
                username='guest',
                email='guest@guest.de',
                password='secureGuestUserPassword'
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
