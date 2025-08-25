from django.urls import path
from .views import ResumeCreateView, ResumeUpdateView

urlpatterns = [
    path("resume/create/", ResumeCreateView.as_view(), name="resume-create"),
    path("resume/<int:id>/edit/", ResumeUpdateView.as_view(), name="resume-edit"),
]