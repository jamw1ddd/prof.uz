from django.urls import path
from apps.professions.views import ProfessionListView, ProfessionDetailView

urlpatterns = [
    path("professions/", ProfessionListView.as_view(), name="profession-list"),
    path("professions/<int:pk>/", ProfessionDetailView.as_view(), name="profession-detail"),
]