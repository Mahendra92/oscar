from __future__ import unicode_literals
from django.db import models
from django_countries.fields import CountryField

class Person(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField(blank_label='(select country)')

# Create your models here.
