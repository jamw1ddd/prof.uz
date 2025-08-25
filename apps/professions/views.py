from rest_framework import generics
from apps.professions.models import Profession, ProfessionDetail
from apps.professions.serializers import ProfessionSerializer, ProfessionDetailSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apps.professions.filters import ProfessionFilter
from rest_framework.filters import OrderingFilter


class ProfessionListView(generics.ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = ProfessionFilter
    ordering_fields = ['name']
    ordering = ['name'] 


class ProfessionDetailView(generics.RetrieveAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer