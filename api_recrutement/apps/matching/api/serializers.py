from rest_framework import serializers
from ..models import Candidate, JobOffer, Skill, MatchScore


from rest_framework import serializers

class MatchingRequestSerializer(serializers.Serializer):
    candidate_id = serializers.IntegerField(help_text="ID du candidat")
    job_id = serializers.IntegerField(help_text="ID de l'offre")





class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class CandidateSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = [
            'id', 'first_name', 'last_name', 'email',
            'experience_years', 'education', 'description', 'skills'
        ]


class JobOfferSerializer(serializers.ModelSerializer):
    required_skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = JobOffer
        fields = [
            'id', 'title', 'company_name', 'location',
            'required_experience', 'description', 'required_skills', 'is_active'
        ]


class MatchScoreSerializer(serializers.ModelSerializer):
    #Champs calculés pour la lisibilité
    candidate_full_name = serializers.SerializerMethodField()
    job_title = serializers.CharField(source='job_offer.title', read_only=True)

    class Meta:
        model = MatchScore
        fields = [
            'id', 'candidate', 'job_offer', 'candidate_full_name',
            'job_title', 'overall_score', 'text_similarity_score',
            'experience_score', 'computed_at'
        ]

    def get_candidate_full_name(self, obj):
        return f"{obj.candidate.first_name} {obj.candidate.last_name}"

