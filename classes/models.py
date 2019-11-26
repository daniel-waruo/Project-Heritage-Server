from django.db import models

from .validators import validate_age, validate_maximum, validate_minimun

"""
Admin(facilitator | curriculum developers | IT Support | child) APP
user-types


TASK
    - Facilitator (id)
    - minAge = models.IntegerField()
    - maxAge = models.IntegerField()
"""


# Create your models here.
class PhClass(models.Model):
    min_age = models.IntegerField(unique=True, validators=(validate_age, validate_minimun))
    max_age = models.IntegerField(unique=True, validators=(validate_age, validate_maximum))
    facilitator = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "( {} - {} )".format(self.min_age, self.max_age)

# class Facilitators(models.Model):
#     firstname = models.CharField(max_length=64)
#     lastname = models.CharField(max_length=64)
