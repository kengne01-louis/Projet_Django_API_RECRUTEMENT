# Projet 6 – API de Recrutement Prédictif

## Description générale

Ce projet consiste à développer une API REST de recrutement prédictif basée sur un moteur de scoring intelligent.
L’API évalue la pertinence d’un candidat pour une offre d’emploi en comparant les profils, les compétences, l’expérience et les descriptions de poste.

Cette première étape concerne : la configuration complète de l’environnement de travail, conformément aux exigences techniques du projet.

---
## Technologies utilisées
Python: 3.10.11 
Django: 4.2.27
Django REST Framework
JWT Authentication (djangorestframework-simplejwt)
Swagger / OpenAPI (drf-spectacular)
Base de données: SQLite (développement)
Git : pour le versioning
uv: pour la gestion des paquets
---

## Structure actuelle du projet

```
djangoProjetSN/
│
├── api/  # Application principale (API REST)
├── config/    # Configuration du projet Django
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── db.sqlite3  # Base de données SQLite
├── manage.py
├── README.md
└── .venv/ # Environnement virtuel (non versionné)
```

---
## Installation et configuration

# Cloner le dépôt

```bash
git clone <url-du-repo>
cd djangoProjetSN
```

## Création et activation de l’environnement virtuel

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Installation de  uv

```bash
pip install uv
```

## Installation des dépendances

```bash
uv pip install django==4.2.27
uv pip install djangorestframework
uv pip install djangorestframework-simplejwt
uv pip install drf-spectacular
```

---
## Authentification JWT
Le projet utilise une authentification JWT pour sécuriser l’API.

Endpoints disponibles :
`POST /api/token/` : obtenir un token
`POST /api/token/refresh/` : rafraîchir le token
---
## Documentation API (Swagger)

documentation interactive est accessible à l’adresse suivante :
[http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
---

## Lancer le projet

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---
## État du projet
Environnement configuré
Django REST + JWT + Swagger opérationnels
---

Projet académique: Système de Recrutement Prédictif
Étudiant: KENGNE Martial.
