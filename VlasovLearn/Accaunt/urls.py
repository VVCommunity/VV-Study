 
from django.urls import path 
from . import views 
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login', views.login_auth,name='login'), 
    path('auth', views.reg,name='auth'),  
    path('restPassword/done/<pk>', views.restPasswordDone,name='restDone'),
    path('restPassword', views.restPassword,name='rest'),    
    path('profile', views.profile_views,name='profile'),  
    path('logout', LogoutView.as_view(next_page='/'), name='logout'), 
    path('balance',  views.balance, name='balance'), 
    path('unitpay',  views.unitpayMethod, name='unitpay'),
    path('success',  views.success, name='success'),
    path('failbuy',  views.failbuy, name='failbuy'),
    path('mycources',  views.mycources, name='mycources'),
    path('pay',  views.pay, name='pay'),
]
