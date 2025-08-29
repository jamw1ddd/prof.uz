import django_filters
from apps.professions.models import Profession

class ProfessionFilter(django_filters.FilterSet):
    min_high = django_filters.NumberFilter(field_name='professiondetail__high', lookup_expr='gte')
    max_high = django_filters.NumberFilter(field_name='professiondetail__high', lookup_expr='lte')
    min_middle = django_filters.NumberFilter(field_name='professiondetail__middle', lookup_expr='gte')
    max_middle = django_filters.NumberFilter(field_name='professiondetail__middle', lookup_expr='lte')
    min_low = django_filters.NumberFilter(field_name='professiondetail__low', lookup_expr='gte')
    max_low = django_filters.NumberFilter(field_name='professiondetail__low', lookup_expr='lte')

    class Meta:
        model = Profession
        fields = ['category', 'min_high', 'max_high', 'min_middle', 'max_middle', 'min_low', 'max_low']
