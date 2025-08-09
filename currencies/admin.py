from django.contrib import admin

from .models import Cryptocurrency


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name', 'rate', 'last_updated')
    search_fields = ('symbol', 'name')
