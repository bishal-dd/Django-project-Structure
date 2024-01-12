from django.db import models


class Service(models.Model):
    description = models.CharField(max_length=5000, null=False)
    rate = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
