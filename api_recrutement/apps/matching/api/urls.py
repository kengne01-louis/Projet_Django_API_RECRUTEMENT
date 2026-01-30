from django.urls import path
from .views import (MatchingCalculateView, BestMatchesView, RecommendationsView, ProfileAnalyzeView)
from . import views

urlpatterns = [

    path('calculate/', MatchingCalculateView.as_view(), name='api-calculate'),
    path('candidates/<int:id>/analyze/', ProfileAnalyzeView.as_view(), name='api-analyze'),
    path('jobs/<int:id>/best-matches/', BestMatchesView.as_view(), name='api-best-matches'),
    path('candidates/<int:id>/recommendations/', RecommendationsView.as_view(), name='api-recommendations'),
    path('', views.MatchingListView.as_view(), name='matching-list'),


]

