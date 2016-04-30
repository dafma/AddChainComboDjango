from django.db import models

# Create your models here.

class State(models.Model):
    contry = models.ForeignKey('country.Country')
    state_name = models.CharField(max_length=100, verbose_name= ('State Name'))

    def __str__(self):
        return self.state_name
