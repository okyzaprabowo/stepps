from __future__ import unicode_literals

from django.db import models

class SteppsResult(models.Model):
    keywords = models.TextField(max_length=1023)
    freq_h = models.IntegerField(default=255)
    px_h = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)