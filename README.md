API de Recrutement Prédictif

 Description
API REST de recrutement prédictif développée avec Django REST Framework. Elle permet d’évaluer automatiquement la compatibilité entre candidats et offres d’emploi grâce à un système de scoring intelligent basé sur l’analyse textuelle, les compétences et l’expérience.

 Consignes Techniques
- Installationde uv : pip install uv
- Framework** : Django 4.2.27 · Django REST Framework (DRF)
- Sécurité & Auth : JSON Web Token (JWT)
- IA & NLP : Scikit-learn (TF-IDF, Cosine Similarity) · spaCy
- Documentation API : Swagger / OpenAPI (drf-spectacular)

Structure du projet
L'architecture suit une approche modulaire pour séparer la logique métier de l'interface API :

```text
api_recrutement/
├── core/                # Configuration globale du projet
│   ├── settings.py      # Config DRF, base de données, apps
│   └── urls.py          # Point d’entrée des URLs
├── apps/                # Dossier des applications Django
│   └── matching/        # Application principale
│       ├── migrations/
│       ├── services/    # IA & Algorithmes (Le "Cerveau")
│       │   ├── nlp_utils.py
│       │   └── scoring.py
│       ├── api/         # Couche API REST (Interface)
│       │   ├── serializers.py
│       │   ├── views.py
│       │   └── urls.py
│       ├── models.py    # Modèles Candidate, JobOffer, Skill
│       └── admin.py
├── manage.py
├── requirements.txt
└── .env
```
État du projet

Environnement configuré Django REST + JWT + Swagger opérationnels



