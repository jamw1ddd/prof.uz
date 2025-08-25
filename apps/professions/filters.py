import django_filters
from apps.professions.models import Profession

class ProfessionFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name="category_id")
    #region = django_filters.NumberFilter(field_name="region_id")

    class Meta:
        model = Profession
        fields = ["category"]  # ,"region"]
