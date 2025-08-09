from rest_framework.routers import DefaultRouter

from .views import CryptocurrencyViewSet

router = DefaultRouter()

router.register(r'cryptocurrencies', CryptocurrencyViewSet, basename='cryptocurrency')

urlpatterns = [] + router.urls
