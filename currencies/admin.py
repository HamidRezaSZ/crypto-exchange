from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Cryptocurrency


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'symbol', 'name', 'rate', 'last_updated')
    search_fields = ('symbol', 'name')
