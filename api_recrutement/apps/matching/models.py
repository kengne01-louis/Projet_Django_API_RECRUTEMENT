from django.db import models

class Skill(models.Model):
    #Compétences techniques (ex: Python, Django, SQL)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    #Profil candidat avec compétences et expérience
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience_years = models.PositiveIntegerField(default=0)
    education = models.CharField(max_length=255)
    description = models.TextField(help_text="Description du profil pour analyse NLP")
    skills = models.ManyToManyField(Skill, related_name="candidates")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class JobOffer(models.Model):
    #Offre d’emploi avec prérequis et localisation
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    required_experience = models.PositiveIntegerField(default=0)
    description = models.TextField(help_text="Détails du poste pour matching TF-IDF")
    required_skills = models.ManyToManyField(Skill, related_name="job_offers")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.company_name}"

class MatchScore(models.Model):
    #Score de compatibilité (0-100) avec détails
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    #Score final pondéré
    overall_score = models.FloatField()
    #Score issu du NLP
    text_similarity_score = models.FloatField()
    #Score issu des années d'expérience
    experience_score = models.FloatField()
    computed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-overall_score']
