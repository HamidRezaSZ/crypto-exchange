from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CryptocurrencyHistoryViewSet, CryptocurrencyViewSet

router = DefaultRouter()

router.register(r'crypto-currencies', CryptocurrencyViewSet, basename='cryptocurrency')


urlpatterns = [
    path(
        'crypto-currencies/<int:currency_id>/history/',
        CryptocurrencyHistoryViewSet.as_view({'get': 'list'}),
        name='cryptocurrency-history',
    ),
] + router.urls
