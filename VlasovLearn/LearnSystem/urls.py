
from django.urls import path 
from . import views 
from django.contrib import admin


urlpatterns = [
    path('', views.home,name='home'), 
    path('chat/<str:room_name>/', views.room, name='room'),
    path('theme/<pk>', views.viewTheme,name='theme'), 
    path('web/<pk>',  views.webinarWelcome, name='web'),
    path('webinar/<pk>',  views.webinar, name='webinar'),
    path('webinars',  views.webinars, name='webinars'),
    path('cource/<pk>',  views.cource, name='cource'),
]