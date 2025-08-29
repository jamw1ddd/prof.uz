from rest_framework import generics
from django.db.models import Max, Min
from apps.professions.models import Profession
from apps.professions.serializers import ProfessionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.professions.filters import ProfessionFilter
from rest_framework.filters import OrderingFilter


class ProfessionListView(generics.ListAPIView):
    serializer_class = ProfessionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProfessionFilter
    ordering_fields = ['category__name', 'max_high', 'min_low']  
    ordering = ['category__name']

    def get_queryset(self):
        return Profession.objects.annotate(
            max_high=Max('professiondetail__high'),
            min_low=Min('professiondetail__low')    
        )

class ProfessionDetailView(generics.RetrieveAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer