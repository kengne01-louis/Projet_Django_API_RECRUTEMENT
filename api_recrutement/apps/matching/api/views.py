from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Candidate, JobOffer, MatchScore
from .serializers import MatchScoreSerializer
from ..services.scoring import calculate_composite_score
from .serializers import MatchingRequestSerializer
from drf_spectacular.utils import extend_schema,OpenApiParameter


class MatchingListView(APIView):
    """
    Vue pour calculer et lister les correspondances entre candidats et offres d'emploi.
    Cette vue interroge la base de données pour fournir des résultats dynamiques.
    """

    @extend_schema(
        parameters=[

            OpenApiParameter(
                name='job_id',
                description="ID de l'offre d'emploi pour laquelle on cherche des candidats",
                required=True,
                type=int
            )
        ],
        responses={200: dict},
        description="Calcule le score de matching entre les candidats et une offre spécifique."
    )
    def get(self, request):
        #1.Récupération de l'ID de l'offre depuis les paramètres de l'URL (?job_id=X)
        job_id = request.query_params.get('job_id')

        #Vérification si le paramètre job_id est présent
        if not job_id:
            return Response(
                {"error": "Le paramètre 'job_id' est obligatoire pour effectuer le matching."},
                status=status.HTTP_400_BAD_REQUEST
            )
        results = []
       # 3. Réponse structurée
        return Response({
            "status": "success",
            "job_offer_id": job_id,
            "count": len(results),
            "matchings": results
        }, status=status.HTTP_200_OK)

#1.POST /api/matching/calculate/
class MatchingCalculateView(APIView):
    serializer_class = MatchingRequestSerializer

    @extend_schema(
        request=MatchingRequestSerializer,
        responses={201: MatchScoreSerializer}
    )
    def post(self, request):
        serializer = MatchingRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        candidate_id = serializer.validated_data['candidate_id']
        job_id = serializer.validated_data['job_id']

        candidate = get_object_or_404(Candidate, id=candidate_id)
        job = get_object_or_404(JobOffer, id=job_id)

        scores = calculate_composite_score(candidate, job)

        match, created = MatchScore.objects.update_or_create(
            candidate=candidate,
            job_offer=job,
            defaults={
                'overall_score': scores.get('overall_score', 0),
                'text_similarity_score': scores.get('text_similarity', 0),
                'experience_score': scores.get('experience_score', 0),
            }
        )

        return Response(
            MatchScoreSerializer(match).data,
            status=status.HTTP_201_CREATED
        )

# 2.GET /api/jobs/{id}/best-matches/
class BestMatchesView(APIView):
    def get(self, request, id):
        job = get_object_or_404(JobOffer, id=id)
        #Optimisation prefetch pour éviter N+1 requêtes
        candidates = Candidate.objects.prefetch_related('skills').all()

        results = []
        for candidate in candidates:
            score_data = calculate_composite_score(candidate, job)
            results.append({
                "candidate_id": candidate.id,
                "name": f"{candidate.first_name} {candidate.last_name}",
                "overall_score": score_data['overall_score']
            })

        #Top 10
        results = sorted(results, key=lambda x: x['overall_score'], reverse=True)[:10]
        return Response(results)


#3.GET /api/candidates/{id}/recommendations/
class RecommendationsView(APIView):
    def get(self, request, id):
        candidate = get_object_or_404(Candidate, id=id)
        jobs = JobOffer.objects.prefetch_related('required_skills').filter(is_active=True)

        recommendations = []
        for job in jobs:
            score_data = calculate_composite_score(candidate, job)
            recommendations.append({
                "job_id": job.id,
                "title": job.title,
                "company": job.company_name,
                "match_score": score_data['overall_score']
            })

        recommendations = sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
        return Response(recommendations)


#4.POST /api/candidates/{id}/analyze/
class ProfileAnalyzeView(APIView):
    """
    Cette vue est générique : elle récupère l'ID du candidat depuis l'URL
    et l'ID du job depuis le corps (JSON) de la requête.
    """

    def post(self, request, id):
        #Récupère dynamiquement le candidat grâce à l'ID passé dans l'URL
        candidate = get_object_or_404(Candidate, id=id)

        #Récupère l'ID du job envoyé dans le JSON
        job_id = request.data.get('job_id')
        if not job_id:
            return Response(
                {"error": "Veuillez fournir un 'job_id' dans le corps JSON."},
                status=status.HTTP_400_BAD_REQUEST
            )

        job = get_object_or_404(JobOffer, id=job_id)

        # Logique de comparaison des compétences
        c_skills = set(candidate.skills.all().values_list('name', flat=True))
        j_skills = set(job.required_skills.all().values_list('name', flat=True))

        missing = list(j_skills - c_skills)

        return Response({
            "analysis": {
                "candidate": f"{candidate.first_name} {candidate.last_name}",
                "job": job.title,
                "missing_skills": missing,
                "advice": f"Apprenez : {', '.join(missing)}" if missing else "Profil parfait !"
            }
        }, status=status.HTTP_200_OK)