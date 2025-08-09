from rest_framework import viewsets

from .models import Cryptocurrency
from .serializers import CryptocurrencyDetailSerializer, CryptocurrencyListSerializer


class CryptocurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cryptocurrency.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CryptocurrencyListSerializer
        return CryptocurrencyDetailSerializer
