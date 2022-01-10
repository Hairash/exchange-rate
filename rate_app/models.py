from django.db import models


class Rate(models.Model):
    btc_usd = models.FloatField()
