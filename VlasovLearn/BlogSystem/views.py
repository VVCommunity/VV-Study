from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    listPosts = BlogBase.objects.all()  
    return render(request, 'BlogSystem/index.html', context = {'posts': listPosts})