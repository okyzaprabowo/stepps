from __future__ import unicode_literals
from django.db import models

# Create your models here.
class SteppsResult(models.Model):
    keyword = models.TextField(max_length=1023)
    freq_high = models.IntegerField(default=255)
    px_high = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    freq_medium = models.IntegerField(default=255)
    px_medium = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    freq_low = models.IntegerField(default=255)
    px_low = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    label = models.CharField(max_length=2, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)