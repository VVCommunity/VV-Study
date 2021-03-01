from django.db import models 
from django.contrib.auth.models import User  
from datetime import datetime
from random import randint
# Create your models here. 
class LearnCource(models.Model): 
    cource_id =  models.PositiveIntegerField(
        default=0,
        verbose_name='Номер курса'
    )
    name = models.CharField(
        max_length=100, 
        verbose_name='Заголовок курса',
        default='Название!' 
    )
    def __str__(self):
        return f"{self.name}, {self.id}"

class LearnModule(models.Model):
    cource = models.ForeignKey(LearnCource, on_delete=models.CASCADE)
     
    name = models.CharField(
        max_length=100, 
        verbose_name='Заголовок модуля',
        default='Название!' 
    ) 
    def __str__(self):
        return f"{self.name}, {self.id}"

class LearnTheme(models.Model):  
    module = models.ForeignKey(LearnModule, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, 
        verbose_name='Тема',
        default='Название!', 
    ) 
    is_Completed = models.BooleanField(verbose_name='Темаы')
    def __str__(self):
        return f"{self.name}, {self.id}"

class ThemeBase(models.Model):   
    theme = models.ForeignKey(LearnTheme, on_delete=models.CASCADE) 
    title = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=100, 
        verbose_name='Описание'
    )
    index =  models.PositiveIntegerField(
        default=0,
        verbose_name='индекс'
    )
    def __str__(self):
        return f"{self.title}, {self.id}"

class ThemeBody(models.Model):   
    theme = models.ForeignKey(LearnTheme, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Текст')
    index =  models.PositiveIntegerField(
        default=0,
        verbose_name='индекс'
    )

class ThemeVideo(models.Model):   
    theme = models.ForeignKey(LearnTheme, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    index =  models.PositiveIntegerField(
        default=0,
        verbose_name='индекс'
    )


class ThemeImage(models.Model):   
    theme = models.ForeignKey(LearnTheme, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='/images/themes/theme_1.png')
  
    description = models.CharField(
        max_length=100, 
        verbose_name='Описание'
    )
    index =  models.PositiveIntegerField(
        default=0,
        verbose_name='индекс'
    )
    def __str__(self):
        return f"{self.description}"

class CourceInstance(models.Model): 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Name  = models.CharField(
        max_length=100, 
        default = 'Курс',
        verbose_name='Описание'
    )
    image = models.ImageField(upload_to='images/', default='/images/themes/theme_1.png')
  
    cource_id =  models.PositiveIntegerField(
        default=0,
        verbose_name='Номер курса'
    ) 
    is_EndCource = models.BooleanField(verbose_name='Курс закончен')

class Message(models.Model): 
    text = models.CharField(max_length=255)  

    def __str__(self):
        """
        Строка для представления сообщения
        """

        return self.text

class Webinar(models.Model): 
    id_webinar =  models.PositiveIntegerField(
        default= randint(0,10000),
        verbose_name='индекс'
    ) 
    title = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=100, 
        verbose_name='Описание'
    )
    url = models.URLField(verbose_name='Zoom')
    image = models.ImageField(upload_to='images/', default='/images/webinar/webinar_1.png')

    created = models.DateTimeField(default=datetime.now, null=True, blank=True, editable=False)

class TicketWebinar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE)

class StatsCource(models.Model):
    cource = models.ForeignKey(CourceInstance, on_delete=models.CASCADE)
    progressToDay =  models.PositiveIntegerField(
        default=0,
        verbose_name='Прогресс за день'
    ) 
    datetime = models.DateTimeField(verbose_name='день')

class EmailClient(models.Model): 
    email =  models.EmailField(verbose_name='Почта клиента');
     
    username = models.CharField(
        max_length=100, 
        verbose_name='Описание'
    )
    

    created = models.DateTimeField(default=datetime.now, null=True, blank=True, editable=False)