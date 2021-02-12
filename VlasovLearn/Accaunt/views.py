from django.shortcuts import render
from .models import * 
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_backends, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q 
from django.http import JsonResponse
# Create your views here.   
import os
import json
import re
import copy
import hashlib
import random as rand
from django.conf import settings 
# Create your views here.

from django import forms
def ksort(d):
	return [[k,d[k]] for k in sorted(d.keys())]
def getSignature(params, method = None ):
		paramss = copy.copy(params)
		if 'signature' in paramss:
			del paramss['signature']
		if 'sign' in paramss:
			del paramss['sign']	
		paramss = ksort(paramss)
		paramss.append([0,'530d0a6557cde8ac2239141352f0672c'])
		if method:
			paramss.insert(0,['method',method])

		#list of dict to str
		res_p = []
		for p in paramss:
			res_p.append(str(p[1]))
		strr = '{up}'.join(res_p)
		strr = strr.encode('utf-8')
		h = hashlib.sha256(strr).hexdigest()
		return h
 
# Create your views here.
def form(publicKey, summ, account, desc, currency='RUB'):
 
    params = {
			'account' : account,
			'currency' : currency,
			'desc' : desc,
			'sum' : summ
		}  
    return getSignature(params)    

@csrf_exempt
def login_auth(request):
        error = ""
        if request.method != "POST":             
            return render(request, 'Accaunt/login.html', context= { 'error':error})
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        print(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
       
        if username is None or password is None:
            return render(request, 'Accaunt/login.html', locals())
        else:
            Newuser = authenticate(username=username, password=password)
        if Newuser is not None:
            if Newuser.is_active:
                login(request,Newuser)
                return HttpResponseRedirect("/")
            else:
                error = "Ошибка аутентификации пользователя"
                return render(request, 'Accaunt/login.html', context= { 'error':error})
        else:
            error = "Неправильный логин или пароль"
            return render(request, 'Accaunt/login.html', context= { 'error':error})

    
def reg(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect('/')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()   
           login(request, user, 'django.contrib.auth.backends.ModelBackend')
           create_profile(request, user)
           return HttpResponseRedirect('/')
        else:
            return render(request=request,template_name="Accaunt/registration.html",context= {'error':{'password2':"",'password':"",'username':""}})
    return render(request=request,template_name="Accaunt/registration.html",context= { 'error':{'password2':"",'password1':"",'username':""}})
   

def profile_views(request): 
    user = User.objects.get(username=request.user)     
    return render(request, 'Accaunt/profile.html' )

def restPassword(request):
  
        if request.method == "POST":
            emailOrLogin = request.POST.get('emailOrLogin',None)
            if(emailOrLogin == None):
                return render(request, 'Accaunt/restPassword.html', context= { 'error': "Пустой email" });
            user = User.objects.get(username=emailOrLogin) 
            if(user == None):
                 user = User.objects.get(email=emailOrLogin) 
                 if(user == None):
                     return render(request, 'Accaunt/restPassword.html', context= { 'error': "Логин или почта не найдены" });
            tocken = restPasswordTocken.objects.create(user = user) 
            tocken.tocken = user.username + str(rand.randint(1,500))
            tocken.save()
            restPass_send_mail("Восстановление доступа: https://www.vvcommunity.ru/account/restPassword/done/"+ tocken.tocken,user.email)        

            return render(request, 'Accaunt/restPassword.html', context= { 'complite': "Проверьте почту: " + user.email })
        return render(request, 'Accaunt/restPassword.html') 
    

def restPass_send_mail(message,email):
    subject = 'Восстановление пароля!' 
    print(send_mail(subject, message,'support@vvcommunity.ru', [email],fail_silently=False))

def restPasswordDone(request,pk):
    tocken = restPasswordTocken.objects.filter(tocken=pk)
    tocken.delete()
    
    return render(request, 'Accaunt/restPasswordDone.html')
def mycources(request):  
    if request.user.is_authenticated != True:
            return HttpResponseRedirect('/')
    purchases = purchase.objects.all();
    cources = []
    for cource in purchases:
        if(cource.userid == request.user.id):
            cources.append(cource)
    data = { "data": cources}
    return render(request, 'Accaunt/cources.html', data)
def failbuy(request):  
     
    user = User.objects.get(username=request.user)  
    
    if request.user.is_authenticated != True:
            return HttpResponseRedirect('/')
    return render(request, 'Accaunt/failbuy.html')
def unitpayMethod(request):  
 
    try: 
 #   if (float(request['orderSum']) != float(orderSum) or
    #    request['orderCurrency'] != orderCurrency or
    #    request['account'] != request.user or
     #   request['projectId'].strip() != str(projectId)):
      #  raise Exception('Order validation Error')
        method = request.GET.get('method',None)
    
        print(method)
        account = request.GET.get('params[account]',None)
        data = {}
        user = User.objects.get(username=account)
        sum = request.GET.get('params[orderSum]')
        hesh = form('249831-a2447', sum,request.user, 'pay', 'RUB')
        unitpayId = request.GET.get('params[unitpayId]',None)
        paymentId = request.GET.get('params[paymentId]',None) 
        if(user == None):
             data = {"error": {
        "message": "User not found str 98"
    }}
             return JsonResponse(data)
        if(method  == 'check'): 
             print("CHECK")
           #  if(hesh != request.GET.get('params[signature]',None)):
             #   data =  {"error": {
      #  "message": "Error signature"
   # }} 
             #   return JsonResponse(data)
        if(method  == 'pay'): 
             print("pay") 
             user.profile.balance += float(sum)
             user.save();
             moneyoper.objects.create(userid=user.id,is_rashod = False, price = float(sum)) 
            
        if(method  == 'error'): 
            data =  {"error": {
        "message": "Error"
    }} 
            return JsonResponse(data)
        
        data = {"result": {
        "message": "Платеж успешно создан.",
        "paymentId": paymentId,  
        "type": "redirect", 
        "redirectUrl": "http://unitpay.money/pay/redirect/249831-a2447" 
    }}; 
        return JsonResponse(data)

    except Exception as e: 
        print(e)
        data = {"error": {
        "message": e
    }}
        return JsonResponse(data)
    #return render(request, data)
def success(request):  
     
    if request.user.is_authenticated !=True:
            return HttpResponseRedirect('/')
         
    return render(request, 'Accaunt/success.html')
def balance(request):  
     
    if request.user.is_authenticated != True:
            return HttpResponseRedirect('/')
         
    opers = moneyoper.objects.all();
    mopersdata = []
    for oper in opers:
        if(oper.userid == request.user.id):
             mopersdata.append(oper)
    data = { "data": mopersdata,"hesh": '', "isPay": False,"sum":'0'}


    return render(request, 'Accaunt/balance.html', data)
@csrf_exempt
def pay(request):
    
    if request.method != "POST":   
        return HttpResponseRedirect('/')
    if request.user.is_authenticated != True:
        return HttpResponseRedirect('/')
    opers = moneyoper.objects.all();
    mopersdata = []
    for oper in opers:
        if(oper.userid == request.user.id):
             mopersdata.append(oper) 
    data = {'hesh': form('249831-a2447', request.POST.get('sum', '0'),request.user, 'pay', 'RUB'),"data": mopersdata,"isPay": True,"sum": request.POST.get('sum', '0')}
     
    return render(request, 'Accaunt/balance.html', data)

def create_profile(request, username):
    if request.method == "POST":
        user = User.objects.get(username=username)    
        user.profile.age = request.POST.get('age', None)
        user.profile.activity = request.POST.get('activity', None)
        user.first_name = request.POST.get('firstName', None)
        user.last_name = request.POST.get('lastName', None)
        user.email  = request.POST.get('email', None)
        user.save() 


def get_activity(activity):
    ACTIVITY_CHOICES = { 'minimal': 'Минимальная активность',
                        'low':'Cлабый уровень активности',
                        'mid': 'Умеренный уровень активности',
                        'high': 'Тяжелая или трудоемкая активность', 
                        'very_high': 'Экстремальный уровень'
    }
    return ACTIVITY_CHOICES.get(activity,'low')
