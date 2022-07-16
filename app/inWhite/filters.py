import django_filters
from .models import *


class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ['name', 'area', 'property_type']

