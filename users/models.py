from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, year):

      user = self.model(username=username, year=year)
      user.set_password(password)
      user.save(using=self._db)
      return user
     

    def create_superuser(self, username, password, year):
        user = self.create_user(username, password=password, year=year)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
      
        return user
    


class CustomUser(AbstractUser):
  
    # username = models.TextField()
    year = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['year'] 

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
      return self.is_admin
    
    