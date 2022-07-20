from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    city = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=255)
    event_date = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=250)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title
