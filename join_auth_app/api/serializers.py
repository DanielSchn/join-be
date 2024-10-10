from rest_framework import serializers
from join_auth_app.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer für das Benutzerprofil.

    Dieser Serializer konvertiert die 'UserProfile'-Daten zwischen Python-Objekten und JSON.

    Felder:
    - **user**: Der zugehörige Benutzer (User), als ForeignKey verknüpft.
    - **initials**: Die Initialen des Benutzers (string), die in der Benutzeroberfläche angezeigt werden.
    - **color**: Eine bevorzugte Farbe des Benutzers (string), die für die Darstellung verwendet werden kann.

    Nutzung:
    - Wird verwendet, um Benutzerprofilinformationen zu erstellen, zu lesen oder zu aktualisieren.
    """
    class Meta:
        model = UserProfile
        fields = ['user', 'initials', 'color']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer für den Benutzer.

    Dieser Serializer konvertiert die 'User'-Daten zwischen Python-Objekten und JSON.

    Felder:
    - **id**: Primärschlüssel (integer), der Benutzer eindeutig identifiziert.
    - **username**: Der Benutzername (string), muss eindeutig sein.
    - **email**: Die E-Mail-Adresse des Benutzers (string), muss ein gültiges Format haben und einzigartig sein.
    - **first_name**: Der Vorname des Benutzers (string), optional.
    - **last_name**: Der Nachname des Benutzers (string), optional.

    Nutzung:
    - Wird verwendet, um Benutzerdaten zu erstellen, zu lesen oder zu aktualisieren.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer zur Registrierung eines neuen Benutzers.

    Dieser Serializer validiert die Eingabedaten für die Registrierung eines Benutzers,
    einschließlich Passwortbestätigung und zusätzlichen Benutzerprofilinformationen.

    Felder:
    - **username**: Der Benutzername (string), muss eindeutig sein.
    - **email**: Die E-Mail-Adresse des Benutzers (string), muss ein gültiges Format haben und einzigartig sein.
    - **password**: Das Passwort des Benutzers (string), muss sicher sein.
    - **repeated_password**: Das Passwort zur Bestätigung (string), darf nur zum Schreiben verwendet werden.
    - **initials**: Die Initialen des Benutzers (string), erforderlich.
    - **color**: Eine bevorzugte Farbe des Benutzers (string), erforderlich.
    - **first_name**: Der Vorname des Benutzers (string), erforderlich.
    - **last_name**: Der Nachname des Benutzers (string), erforderlich.

    Validierung:
    - Stellt sicher, dass das Passwort und das wiederholte Passwort übereinstimmen.
    - Überprüft, ob bereits ein Benutzer mit der angegebenen E-Mail-Adresse registriert ist.

    Nutzung:
    - Die Methode 'save()' erstellt einen neuen Benutzer und ein zugehöriges Benutzerprofil.
    """
    repeated_password = serializers.CharField(write_only=True)
    initials = serializers.CharField(required=True, write_only=True)
    color = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password', 'initials', 'color', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        """
        Speichert einen neuen Benutzer und erstellt ein zugehöriges Benutzerprofil.

        :raises ValidationError: Wenn die Passwörter nicht übereinstimmen oder wenn die E-Mail bereits verwendet wird.
        """
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        initials = self.validated_data['initials']
        color = self.validated_data['color']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        if pw != repeated_pw:
            raise serializers.ValidationError({'error':'passwords dont match'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'user already registered with this email'})
        account = User(email=self.validated_data['email'], username=self.validated_data['username'], first_name=first_name, last_name=last_name)
        account.set_password(pw)
        account.save()

        UserProfile.objects.create(
            user=account,
            initials=initials,
            color=color,
        )
        return account