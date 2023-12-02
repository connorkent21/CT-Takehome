from django.db import models


class Example(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)