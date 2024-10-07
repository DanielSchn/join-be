from rest_framework import generics, viewsets
from join_auth_app.models import UserProfile
from .serializers import UserProfileSerializer, RegistrationSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CustomLoginView(ObtainAuthToken):
    """
    Benutzerdefinierte Login-View, die Authentifizierung basierend auf E-Mail und Passwort ermöglicht.

    - 'POST': Authentifiziert einen Benutzer und gibt das Auth-Token sowie Benutzerdetails zurück.
    
    Anforderungen:
    - 'email': Die E-Mail-Adresse des Benutzers.
    - 'password': Das Passwort des Benutzers.
    
    Rückgabe:
    - Bei erfolgreicher Authentifizierung: Ein JSON-Objekt mit dem Token und Benutzerdetails ('token', 'username', 'email', 'first_name', 'last_name', 'id').
    - Bei fehlgeschlagener Authentifizierung: Ein Fehler-JSON mit der Nachricht "Invalid email or password".
    
    Berechtigungen:
    - Keine Authentifizierung erforderlich ('AllowAny').
    """
    permission_classes = [AllowAny]

    def post(self, request, *arg, **kwarg):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=400)
        user = authenticate(request=request, username=user.username, password=password)
        if not user:
            return Response({'error': 'Invalid email or password'}, status=400)
        data = {}
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'id': user.id
        }
        return Response(data)


class RegistrationView(APIView):
    """
    API-View zur Registrierung eines neuen Benutzers.

    - 'POST': Registriert einen neuen Benutzer basierend auf den bereitgestellten Daten und gibt das Authentifizierungstoken sowie die Benutzerdaten zurück.
    
    Anforderungen:
    - 'username': Benutzername des neuen Benutzers.
    - 'email': E-Mail-Adresse des neuen Benutzers.
    - 'password': Passwort des neuen Benutzers.

    Rückgabe:
    - Bei erfolgreicher Registrierung: Ein JSON-Objekt mit dem Auth-Token und Benutzerdetails ('token', 'username', 'email').
    - Bei ungültigen Daten: Eine Fehlerbeschreibung, welche Felder ungültig sind.

    Berechtigungen:
    - Keine Authentifizierung erforderlich ('AllowAny').
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
        else:
            data = serializer.errors
        return Response(data)
    