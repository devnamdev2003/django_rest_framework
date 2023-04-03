from django.db import models


class StudentData(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    roll = models.CharField(max_length=200)
