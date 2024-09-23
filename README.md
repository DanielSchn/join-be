# Backend for JOIN Project

Ein Backend-Projekt zum speichern der Daten aus dem Frontend-Projekt JOIN der Developer Akademie. Das Projekt wurde im Frontend-Kurs mit der Database von Firebase realisiert.

## Funktionen
- User registrieren mit Name, Mail und Passwort.
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
"env/Scripts/activate"
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
Nachdem der Server läuft, kannst du die API verwenden, um Posts zu erstellen, zu liken, zu kommentieren und den Feed anzusehen. Hier einige nützliche Befehle:

- Starte den Entwicklungsserver:
```
python manage.py runserver
```
- Migriere die Datenbank:
```
python manage.py makemigrations
python manage.py migrate
```

## Deployment
Für dieses Projekt gibt es derzeit keine spezifischen Deployment-Anweisungen.

## Lizenz
Dieses Projekt wurde als Teil eines Lernprojekts erstellt und steht ohne spezifische Lizenz zur Verfügung.
