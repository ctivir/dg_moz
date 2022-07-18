from django.db import models


class event(models.Model):
    city = models.CharField(max_length=250)
    date = models.DateTimeField('date')
    image = models.CharField(max_length=250)
