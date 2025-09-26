from django.db import models


class Widget(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=140, null=True)
