from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BlogBase) 
admin.site.register(BlogText)    
admin.site.register(BlogImage)    