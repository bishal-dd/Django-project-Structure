from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, null=True)
    logo_image = models.TextField(null=True)
    phone_no = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    signature_image = models.TextField(null=True)
    manual_signature_image = models.CharField(max_length=20000, null=True)
    slug = models.SlugField(null=False)
