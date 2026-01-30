## API DE RECRUTEMENT PRÉDICTIF À L'AIDE D'UN MODÈLE DE SCORING


# 1- Situation contexte du Projet:

Le marché de l'emploi de plus en plus dynamique, la rapidité et la précision du matching entre les talents et les opportunités sont cruciales. Ce projet consiste a concevoir une  API REST avec Django Rest Framework (DRF), pour automatiser et optimiser le processus de présélection des candidats.
L'objectif est de dépasser la simple recherche par mots-clés en utilisant des techniques de Machine Learning (TF-IDF) pour évaluer la compatibilité réelle entre le profil d'un candidat et les exigences spécifiques d'une offre d'emploi.


# 2- Le Modèle de Scoring.
C'est le coeur du système qui repose sur un algorithme de scoring en temps reel qui calcule un score de compatibilité (MatchScore) compris entre 0 et 100: CE QUI PERMET  DE QUANTIFIER LA PERTINENCE  D'UNE CANDIDATURE DE MANIERE OBJECTIVE.


# 3- Composition du Score Composite:

Le score final est calculé selon trois piliers fondamentaux pondérés :
- Similarité Textuelle (50%) : Utilisation de la vectorisation TF-IDF (TfidfVectorizer) et de la similarité cosinus (cosine_similarity) pour comparer les descriptions textuelles des postes avec les parcours des candidats. Cela permet de mesurer l'affinité sémantique entre les deux documents.
- Overlap des Compétences (30%) : Calcul mathématique basé sur l'intersection des compétences techniques (Skills) possédées par le candidat et celles requises par l'offre. Plus le candidat possède de "Hard Skills" demandées, plus ce score est élevé.
- Expérience (20%) : Évaluation de la correspondance entre les années d'expérience ou le niveau de séniorité du candidat et les attentes du recruteur définies dans l'offre.

# 4- Résultat en sortie:

Pour chaque analyse, l'API retourne un objet JSON détaillé contenant :
- Le Score global (0-100).
- Le Détail par critère (pour comprendre pourquoi un candidat matche ou non).
- Une Analyse prédictive incluant des suggestions d'amélioration pour le candidat (compétences manquantes à acquérir).


# 5- Consignes Techniques

- Installationde uv : pip install uv
- Framework : Django 4.2.27 · Django REST Framework (DRF)
- Sécurité & Auth : JSON Web Token (JWT)
- IA & NLP : Scikit-learn (TF-IDF, Cosine Similarity) · spaCy
- Documentation API : Swagger / OpenAPI (drf-spectacular)


# 6- Endpoints Principaux

| Méthode | Endpoint                                   | Description |
|--------:|--------------------------------------------|-------------|
| POST    | `/api/matching/calculate/`                 | Calcule le score de match entre un `candidate_id` et un `job_id`. |
| GET     | `/api/jobs/{id}/best-matches/`             | Retourne le Top 10 des meilleurs candidats pour une offre spécifique. |
| GET     | `/api/candidates/{id}/recommendations/`   | Suggère les meilleures offres d'emploi pour un candidat donné. |
| POST    | `/api/candidates/{id}/analyze/`            | Analyse le profil et génère des conseils d'amélioration. |



## 7- Préparation de l'environnement

# Créer l'environnement virtuel
python -m venv .venv
# Activer l'environnement 
.venv\Scripts\activate
# Activer l'environnement 
source .venv/bin/activate


# 8- Installation des dépendances
 pip install -r requirements.txt


## 8- Configuration de la base de données (Migrations)

# Préparer les fichiers de migration
python manage.py makemigrations
# Appliquer les migrations à la base de données
python manage.py migrate
# Création d'un compte d'Administrateur
python manage.py createsuperuser
# Lancement de l'API
python manage.py runserver


# 9- Structure du projet
Dans l'architecture suivante , nous avons utiliser une approche modulaire  qui permet de séparer la logique métier de l'interface API :

```text
api_recrutement/
├── core/                              # Configuration globale du projet
│   ├── settings.py                     # Config DRF, base de données, apps
│   └── urls.py                         # Point d’entrée des URLs
├── apps/                                # Dossier des applications Django
│   └── matching/                        # Application principale
│       ├── migrations/
│       ├── services/                    # IA & Algorithmes (Le "Cerveau")
│       │   ├── nlp_utils.py
│       │   └── scoring.py
│       ├── api/                         # Couche API REST (Interface)
│       │   ├── serializers.py
│       │   ├── views.py
│       │   └── urls.py
│       ├── models.py                    # Modèles Candidate, JobOffer, Skill
│       └── admin.py
├── manage.py
├── requirements.txt
└── .env
```




