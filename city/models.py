from django.db import models

# Create your models here.

class City(models.Model):
    state = models.ForeignKey('state.State')
    city_name = models.CharField(max_length=100, verbose_name= ('City Name'))

    def __str__(self):
        return self.city_name

