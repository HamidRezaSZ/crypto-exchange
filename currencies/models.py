from django.db import models
from simple_history.models import HistoricalRecords


class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=20, decimal_places=8)
    last_updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    class Meta:
        ordering = ['-name']
