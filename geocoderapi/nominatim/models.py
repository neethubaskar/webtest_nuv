from django.db import models

# Create your models here.

class Locaions(models.Model):
    location_name = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.location_name