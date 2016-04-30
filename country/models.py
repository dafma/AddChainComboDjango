from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=100, verbose_name= ('Country name'))

    def __str__(self):
        return self.country_name

