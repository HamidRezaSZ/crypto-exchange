from django_filters.rest_framework import DateTimeFilter, FilterSet, NumberFilter

from .models import Cryptocurrency


class CryptocurrencyFilter(FilterSet):
    rate__gt = NumberFilter(field_name='rate', lookup_expr='gt')
    rate__lt = NumberFilter(field_name='rate', lookup_expr='lt')
    last_updated__gt = DateTimeFilter(field_name='last_updated', lookup_expr='gt')
    last_updated__lt = DateTimeFilter(field_name='last_updated', lookup_expr='lt')

    class Meta:
        model = Cryptocurrency
        fields = ['rate__gt', 'rate__lt', 'last_updated__gt', 'last_updated__lt']


class CryptocurrencyHistoryFilter(FilterSet):
    rate__gt = NumberFilter(field_name='rate', lookup_expr='gt')
    rate__lt = NumberFilter(field_name='rate', lookup_expr='lt')
    last_updated__gt = DateTimeFilter(field_name='last_updated', lookup_expr='gt')
    last_updated__lt = DateTimeFilter(field_name='last_updated', lookup_expr='lt')

    class Meta:
        model = Cryptocurrency.history.model
        fields = ['rate__gt', 'rate__lt', 'last_updated__gt', 'last_updated__lt']
