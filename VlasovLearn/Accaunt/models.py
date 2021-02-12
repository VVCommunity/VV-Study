from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User  
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError 
# Create your models here.

class profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    cover = models.ImageField(upload_to='images/', default='/images/icon_0.png')
  
    is_teacher = models.BooleanField(default=False,verbose_name='Преподаватель')
 
 
    #Метод создаёт данные пользователя       
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

    #Метод сохраняет данные пользователя или создаёт их       
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs): 
        print("Saving profile")
        if instance.profile is not None:
            print("Save profile")
            instance.profile.save()
        else:  
            profile.objects.create(user=instance)
  
class restPasswordTocken(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tocken = models.CharField(
        max_length=200, 
        verbose_name='Токен авторизации'
    )
    
    created = models.DateTimeField(default=datetime.now, null=True, blank=True, editable=False)