import requests
from celery import shared_task
from django.conf import settings

from currencies.models import Cryptocurrency


@shared_task
def update_cryptocurrencies_from_api():
    """
    Fetches cryptocurrency rates from CoinGecko and updates/creates Cryptocurrency objects in the DB.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 50,
        'page': 1,
        'sparkline': 'false',
    }
    headers = {'x-cg-demo-api-key': settings.CRYPTO_CURRENCY_API_KEY}

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return
    data = response.json()
    for coin in data:
        Cryptocurrency.objects.update_or_create(
            symbol=coin['symbol'].upper(),
            defaults={
                'name': coin['name'],
                'rate': coin['current_price'],
            },
        )
