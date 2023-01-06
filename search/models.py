from django.conf import settings
from django.db import models
from django.urls.base import reverse

# Create your models here.

class Jobs(models.Model):
    job_title = models.CharField(max_length=500)
    job_company = models.CharField(max_length=500)
    job_location = models.CharField(max_length=500)
    job_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.job_title

