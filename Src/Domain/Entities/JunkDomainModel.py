from django.db import models
from django.contrib import admin


class JunkDomainModel(models.Model):
    temp = models.CharField(max_length=100, blank=False, null=False)



