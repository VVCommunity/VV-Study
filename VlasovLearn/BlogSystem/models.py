from django.db import models

from django.contrib.auth.models import User  
# Create your models here.

class BlogBase(models.Model):    
    title = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=100, 
        verbose_name='Описание'
    )
    preview = models.ImageField(upload_to='images/', default='/images/blog/blog_1.png')
    index =  models.PositiveIntegerField(
        default=0,
        verbose_name='индекс'
    )
    def __str__(self):
        return f"{self.title}, {self.id}"


class BlogText(models.Model):   
    blog = models.ForeignKey(BlogBase, on_delete=models.CASCADE) 
    text = models.TextField(
        
        verbose_name='Text'
    )
    index =  models.PositiveIntegerField(
        default=0,
        verbose_name='индекс'
    )
    def __str__(self):
        return f"{self.blog.title}, {self.id}"


class BlogImage(models.Model):   
    blog = models.ForeignKey(BlogBase, on_delete=models.CASCADE) 
    
    image = models.ImageField(upload_to='images/', default='/images/blog/blog_1.png')
    index =  models.PositiveIntegerField(
        default=0,
        verbose_name='индекс'
    )
    def __str__(self):
        return f"{self.blog.title}, {self.id}"