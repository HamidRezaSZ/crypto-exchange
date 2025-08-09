from rest_framework import serializers

from .models import Cryptocurrency


class CryptocurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['id', 'symbol', 'name', 'rate']


class CryptocurrencyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['id', 'symbol', 'name', 'rate', 'last_updated']
