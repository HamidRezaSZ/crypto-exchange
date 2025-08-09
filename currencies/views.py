from django.shortcuts import get_object_or_404
from django_filters.rest_framework import (
    DateTimeFilter,
    DjangoFilterBackend,
    FilterSet,
    NumberFilter,
)
from rest_framework import filters, mixins, viewsets

from .models import Cryptocurrency
from .serializers import (
    CryptocurrencyDetailSerializer,
    CryptocurrencyHistorySerializer,
    CryptocurrencyListSerializer,
)


class CryptocurrencyFilter(FilterSet):
    rate__gt = NumberFilter(field_name='rate', lookup_expr='gt')
    rate__lt = NumberFilter(field_name='rate', lookup_expr='lt')
    last_updated__gt = DateTimeFilter(field_name='last_updated', lookup_expr='gt')
    last_updated__lt = DateTimeFilter(field_name='last_updated', lookup_expr='lt')

    class Meta:
        model = Cryptocurrency
        fields = ['rate__gt', 'rate__lt', 'last_updated__gt', 'last_updated__lt']


class CryptocurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cryptocurrency.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_class = CryptocurrencyFilter
    search_fields = ['symbol', 'name']

    def get_serializer_class(self):
        if self.action == 'list':
            return CryptocurrencyListSerializer
        return CryptocurrencyDetailSerializer


class CryptocurrencyHistoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CryptocurrencyHistorySerializer
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'currency_id'
    filterset_class = CryptocurrencyFilter

    def get_queryset(self):
        currency_id = self.kwargs.get('currency_id')
        return get_object_or_404(Cryptocurrency, id=currency_id).history.all()
