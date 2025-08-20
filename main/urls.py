from django.urls import path, include
from .views import starter_view

urlpatterns = [
    path('starters/', starter_view, name='starter-view'),
]
