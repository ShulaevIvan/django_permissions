from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter
from rest_framework.filters import SearchFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()
    creator = SearchFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'updated_at']
