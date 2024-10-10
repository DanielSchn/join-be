# Backend for JOIN Project

Ein Backend-Projekt zum speichern der Daten aus dem Frontend-Projekt JOIN der Developer Akademie. Das Projekt wurde im Frontend-Kurs mit der Database von Firebase realisiert.

## Funktionen
- User registrieren mit Name, Mail und Passwort.
- Eigenen User bearbeiten: Vorname, Nachname und Email
- Kanban Tasks erstellen, bearbeiten und löschen
- Kontakte anlegen, bearbeiten und löschen

## Voraussetzungen
- Python (Version 3.x)
- Django (Version und zusätzliche Pakete siehe requirements.txt)
- Django CORS Headers
- JOIN Frontend https://github.com/DanielSchn/join-fe

Alles benötigte kann über die requirements.txt installiert werden. (Siehe Punkt 3)

## Installation
### 1. Projekt klonen
```
git clone git@github.com:DanielSchn/join-be.git
cd join-be
```
### 2. Virtual Environment erstellen
Virtuelles Python-Umfeld erstellen und aktivieren
```
python -m venv env
source env/bin/activate # Linux/Mac
"env/Scripts/activate" # Windows
```
### 3. Abhängigkeiten installieren
```
pip install -r requirements.txt
```
### 4. Django-Projekt initialisieren
Datenbank migrieren und Server starten
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Projekt läuft, je nach Konfiguration, unter `http://127.0.0.1:8000`.

## Konfiguration
In der Datei `settings.py` wurden einige wichtige Einstellungen vorgenommen, um das Projekt lokal auszuführen:
```
ALLOWED_HOSTS = ['127.0.0.1']
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:5500',
    'http://localhost:5500'
]
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5500',
    'http://localhost:5500'
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
Diese Einstellungen ermöglichen Cross-Origin-Anfragen vom lokalen Frontend, das auf `localhost:5500` läuft.

## Nutzung
Nachdem der Server läuft, kann die API verwendet werden, um User zu registrieren, sich einzuloggen, Task zu erstellen / ändern / löschen, Kontakte erstellen / ändern / löschen.<br>
Hier einige nützliche Befehle:

- Starte den Entwicklungsserver:
```
python manage.py runserver
```
### Nach der Ersten Einrichtung muss der Gast User manuell erstellt werden. Dies kann auf drei Wege realisiert werden.

#### 1. Über ein custom management command

- Dafür muss nur folgende Zeile im Terminal ausgeführt werden:
```
python manage.py create_guest_user
```

#### 2. Weg über das Terminal und die Shell von Django

- Dafür folgende Befehle im Terminal eingeben:
```
python manage.py shell
from django.contrib.auth.models import User
from join_auth_app.models import UserProfile
```
- Dann folgende Befehle komplett in die Shell kopieren. Diese werden dann automatisch nacheinander ausgeführt. Nach der letzten Zeile muss evtl. noch die Return Tast auf der Tastatur einmal bestätigt werden:
```
account = User.objects.create_user(username='guest', email='guest@guest.de', password='guest')
account.first_name = 'Guest'
account.last_name = 'User'
account.save()
initials = 'GU'
color = '#DC3DF5'
UserProfile.objects.create(user=account, initials=initials, color=color)
```

#### 3. Weg über das Frontend einen User registrieren
- Oben rechts auf Sign up klicken und folgende Daten nutzen:
```
Full Name: Guest User
Email: guest@guest.de
Password: guest
Confirm Password: guest
```

## Deployment
Für dieses Projekt gibt es derzeit keine spezifischen Deployment-Anweisungen.

## Lizenz
Dieses Projekt wurde als Teil eines Lernprojekts erstellt und steht ohne spezifische Lizenz zur Verfügung.
