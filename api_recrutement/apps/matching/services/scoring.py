from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .nlp_utils import preprocess_text


def calculate_composite_score(candidate, job_offer):
    """ score global selon les 3 critères pondérés"""

    #1.Score Textuel (50%) : TF-IDF + Cosine Similarity
    # Nettoyage des descriptions
    candidate_clean = preprocess_text(candidate.description)
    job_clean = preprocess_text(job_offer.description)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([candidate_clean, job_clean])

    #Calcul de la similarité cosinus entre les deux vecteurs
    score_text = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    #2.Score Skills (30%) : Intersection des listes
    c_skills = set(candidate.skills.all().values_list('name', flat=True))
    j_skills = set(job_offer.required_skills.all().values_list('name', flat=True))

    if not j_skills:
        score_skills = 1.0
    else:
        #Taux de recouvrement des compétences
        score_skills = len(c_skills.intersection(j_skills)) / len(j_skills)

    #3.Score Expérience (20%) : Proximité
    # Calcul de l'écart entre expérience réelle et requise
    diff = abs(candidate.experience_years - job_offer.required_experience)
    # On perd 10% de score par année d'écart
    score_exp = max(0, 1 - (diff / 10))

    #Calcul Final Pondéré
    overall_score = (score_text * 0.5) + (score_skills * 0.3) + (score_exp * 0.2)

    return {
        "overall_score": round(overall_score * 100, 2),
        "text_similarity": round(score_text * 100, 2),
        "skill_overlap": round(score_skills * 100, 2)
    }