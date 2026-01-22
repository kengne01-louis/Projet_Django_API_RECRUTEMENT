```markdown
# API DE RECRUTEMENT PREDICTIF

## Description
API REST de recrutement prédictif** développée avec Django REST Framework.  
Elle permet d’évaluer automatiquement la compatibilité entre candidats et offres d’emploi grâce à un système de scoring intelligent basé sur l’analyse textuelle, les compétences et l’expérience.

## Consignes Technique
- **Framework** : Django 4.2.27 · Django REST Framework (DRF)
- **Sécurité & Auth** : JSON Web Token (JWT)
- **IA & NLP** : Scikit-learn (TF-IDF, Cosine Similarity) · spaCy
- **Documentation API** : Swagger / OpenAPI (drf-spectacular)

## Structure du projet
```

api_recrutement/
├──api_recrutement /      # Configuration globale du projet
│   ├── settings.py            # Config DRF, base de données, apps
│   └── urls.py        # Point d’entrée des URLs
│
├── apps/          applications Django
│   └── matching/          # Application principale
│       ├── migrations/
│       ├── services/        # IA & Algorithmes
│       │   ├── nlp_utils.py    # Prétraitement texte (spaCy)
│       │   └── scoring.py     # TF-IDF, Cosine Similarity, scoring
│       ├── api/          # Couche API REST
│       │   ├── serializers.py
│       │   ├── views.py
│       │   └── urls.py
│       ├── models.py       # Candidate, JobOffer, Skill, MatchScore
│       └── admin.py        # Interface admin
│
├── manage.py
├── requirements.txt
└── .env

```

