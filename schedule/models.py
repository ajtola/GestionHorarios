from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Schedule(models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField(blank=True, null=True)
    hours_worked = models.DurationField(blank=True, null=True)
    worker = models.ForeignKey(User)