from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from whatthegam.models import School

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)   
#     year = models.IntegerField(null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     def __str__(self):   
#         return f'id={self.id}, user_id={self.user.id}, year={self.year}'

#     def update_date(self): 
#         self.updated_at = timezone.now()
#         self.save()
    
#     @receiver(post_save, sender=User)  
#     def create_user_profile(sender, instance, created, **kwargs):        
#         if created:          
#             Profile.objects.create(user=instance)  
    
#     @receiver(post_save, sender=User)  
#     def save_user_profile(sender, instance, **kwargs):        
#         instance.profile.save()




