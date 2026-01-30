from django.contrib import admin
from .models import Candidate, JobOffer, Skill, MatchScore

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'experience_years')
    search_fields = ('last_name', 'email')
    #Facilite la sélection des compétences
    filter_horizontal = ('skills',)

@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'is_active')
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'company_name')
    filter_horizontal = ('required_skills',)

@admin.register(MatchScore)
class MatchScoreAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job_offer', 'overall_score', 'computed_at')
    readonly_fields = ('computed_at',)
