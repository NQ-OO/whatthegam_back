

from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    map_id = models.CharField(max_length=50) #지도 api가 갖고 있는, 장소에 대한 고유 id값. 

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    

