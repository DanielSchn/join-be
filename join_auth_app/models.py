from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    """
    Modell für Benutzerprofile.

    Dieses Modell speichert zusätzliche Informationen über einen Benutzer,
    die über die Standardbenutzerinformationen hinausgehen.

    Felder:
    - **user**: Ein 'OneToOneField', der mit dem zugehörigen 'User'-Objekt verknüpft ist.
      Wenn der Benutzer gelöscht wird, wird auch das zugehörige Profil gelöscht.
    - **initials**: Ein 'CharField', das die Initialen des Benutzers speichert.
      Es hat eine maximale Länge von 2 Zeichen.
    - **color**: Ein 'CharField', das eine bevorzugte Farbe des Benutzers speichert.
      Es hat eine maximale Länge von 10 Zeichen.

    Methoden:
    - **__str__()**: Gibt den Benutzernamen des zugehörigen Benutzers zurück, um eine lesbare
      Darstellung des Profils zu ermöglichen.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initials = models.CharField(max_length=2)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username