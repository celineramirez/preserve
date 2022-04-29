from django.db import models
from django.conf import settings

class Habitat(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.URLField(max_length=200)
    history = models.TextField(null=True)
    threats = models.TextField(null=True)
    invasive_species = models.TextField(null=True)
    conservation_strategies = models.TextField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name