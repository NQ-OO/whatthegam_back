

from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User


class School(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name