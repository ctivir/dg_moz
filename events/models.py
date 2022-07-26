from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    city = models.CharField(max_length=250)
    #address = models.CharField("Full address", max_length=1024, default="XPO")
    slug = models.SlugField(unique=True, max_length=255)
    event_date = models.DateTimeField(default=timezone.now)
    image = models.URLField(default="https://live.staticflickr.com/65535/52228664276_737e194b98_4k.jpg")
    url = models.URLField(default="https://djangogirls.org/en/matola/")
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=250)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title
