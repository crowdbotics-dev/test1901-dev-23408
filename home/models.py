from django.conf import settings
from django.db import models


class Home(models.Model):
    "Generated Model"
    name = models.TextField()


class Home1(models.Model):
    "Generated Model"
    name = models.BigIntegerField()
