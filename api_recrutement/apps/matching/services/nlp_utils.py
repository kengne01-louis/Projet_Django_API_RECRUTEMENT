import spacy

# Chargement du modèle français
try:
    nlp = spacy.load("fr_core_news_sm")
except OSError:
    nlp = None


def preprocess_text(text):
    #Nettoyage du texte : minuscule, retrait ponctuation et mots vides
    if not text or nlp is None:
        return text or ""

    doc = nlp(text.lower())
    #On ne garde que les mots significatifs (pas de ponctuation, pas de stop words)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)