from django.db import models 
from django.contrib.auth.models import User  
from datetime import datetime
# Create your models here. 
# Create your models here.
class TapLink(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100, 
        verbose_name='Описание'
    )
    url = models.URLField(verbose_name='Профил')
     
    
    created = models.DateTimeField(default=datetime.now, null=True, blank=True, editable=False)

class TapButton(models.Model): 
    tap = models.ForeignKey(TapLink,on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100, 
        verbose_name='Название'
    )
    url = models.URLField(verbose_name='ссылка')
     