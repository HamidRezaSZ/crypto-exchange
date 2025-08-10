from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from .filters import CryptocurrencyFilter, CryptocurrencyHistoryFilter
from .models import Cryptocurrency
from .serializers import (
    CryptocurrencyDetailSerializer,
    CryptocurrencyHistorySerializer,
    CryptocurrencyListSerializer,
)


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

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class CryptocurrencyHistoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CryptocurrencyHistorySerializer
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'currency_id'
    filterset_class = CryptocurrencyHistoryFilter

    def get_queryset(self):
        currency_id = self.kwargs.get('currency_id')
        return get_object_or_404(Cryptocurrency, id=currency_id).history.all()

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
