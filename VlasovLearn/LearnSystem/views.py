from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Sum, Avg, Count
from django.shortcuts import render
from .models import * 
from django.http import Http404,HttpResponseRedirect,HttpResponsePermanentRedirect,HttpResponse
from django.core.mail import send_mail, BadHeaderError 
from qsstats import QuerySetStats
from django.template import loader
# Create your views here.

def home(request):
    if request.user.is_authenticated == False:
            return HttpResponseRedirect('/accounts/login')
    
    user = User.objects.get(username=request.user)  
    courcesInstance = CourceInstance.objects.filter(user = user)
    listCource = []
  
    for cource in courcesInstance: 
        cources = LearnCource.objects.filter(cource_id = cource.cource_id) 
        modules = LearnModule.objects.filter(cource_id = cource.cource_id)
        
        modulesList = []
        for module in modules:
            themes = LearnTheme.objects.filter(module_id = module.id) 
             
            moduleData = {'module': module,'themes': themes} 
            modulesList.append(moduleData)
        
        courceDirectory = {'cources': cources,'modulesList': modulesList}
        listCource.append(courceDirectory)  
        
    
    return render(request,'LearnSystem/index.html',context={'listcources':listCource,'theme':''})


def viewTheme(request,pk):
    if request.user.is_authenticated == False:
            return HttpResponseRedirect('/account/login')
    
    user = User.objects.get(username=request.user)  
    courcesInstance = CourceInstance.objects.filter(user = user)
    listCource = []
  
    for cource in courcesInstance: 
        cources = LearnCource.objects.filter(cource_id = cource.cource_id) 
        modules = LearnModule.objects.filter(cource_id = cource.cource_id)
        
        modulesList = []
        for module in modules:
            themes = LearnTheme.objects.filter(module_id = module.id)
            moduleData = {'module': module,'themes': themes} 
            modulesList.append(moduleData)
        
        courceDirectory = {'cources': cources,'modulesList': modulesList}
        listCource.append(courceDirectory)  
    theme = LearnTheme.objects.get(pk=pk);
    if theme: 
        themeListData = []
        themeData = {'theme': theme, 'listData': themeListData } 
        bases = theme.themebase_set.all()
        for x in bases:
            themeListData.insert(x.index,{'base': x})
        bodys = theme.themebody_set.all()
        for x in bodys:
            themeListData.insert(x.index,{'body': x})
        images = theme.themeimage_set.all()
        for x in images:
            themeListData.insert(x.index,{'image': x})
        videos = theme.themevideo_set.all() 
        for x in videos:
            themeListData.insert(x.index,{'video': x})
        
        return render(request,'LearnSystem/index.html',context={'listcources':listCource,'themeData':themeData})     
                
    return render(request,'LearnSystem/index.html',context={'listcources':listCource})

def welcomeweb(request, pk): 
    webinar = Webinar.objects.get(pk=pk)
    message = ""
    if request.method != "POST":             
        return render(request, 'LearnSystem/welcomeWebinar.html',  context = { 'message':message,'webinar':webinar})
    
    if(webinar == None):
        return HttpResponseRedirect('/')
    if request.user.is_authenticated == False: 
        return render(request, 'LearnSystem/welcomeWebinar.html', context= { 'message':message,'webinar':webinar})
                
    return render(request, 'LearnSystem/welcomeWebinar.html', context= { 'message':message,'webinar':webinar})

def webinarWelcome(request, pk):  
    webinar = Webinar.objects.get(id_webinar=int(pk))
    if request.method != "POST":
        return render(request, 'LearnSystem/welcomeWebinar.html', context= { 'webinar': webinar})
    
    if request.user.is_authenticated != False:
        user = User.objects.get(username=request.user)  
        TicketWebinar.objects.create(user=user,webinar=webinar)
    username = request.POST.get('name', 'студент')
    email = request.POST.get('email', None)
    if(email == None):
        return render(request, 'LearnSystem/welcomeWebinar.html', context= { 'webinar':webinar, 'message':'Проверьте почту.'}) 
    message = 'Запись на вебинар ' + webinar.title
    web_send_mail(username,message,webinar.url,email)
    
    return render(request, 'LearnSystem/welcomeWebinar.html', context= { 'webinar':webinar, 'message':'Приглашение на вашей почте!'}) 

def webinar(request, pk):  
    
    user = User.objects.get(username=request.user)  
    webinars = user.ticketwebinar_set.all()

    for ticket in webinars:
        if(ticket.webinar.guid == pk):
            return render(request, 'LearnSystem/webinar.html', context= { 'webinar':ticket.webinar})
 
    return HttpResponseRedirect('/') 

def web_send_mail(username,message,url,email):
    subject = 'Вебинар Виталия скоро начнётся!' 
    html_message = loader.render_to_string(
            'LearnSystem/EmailMSGWebinar.html',
            {
                'user_name': username,
                'subject':  message, 
                'url': url
            }
        )
    print(send_mail(subject, message,'support@vvcommunity.ru', [email],fail_silently=False,html_message=html_message))

def room(request, room_name):
    return render(request, 'LearnSystem/chat.html', {
        'room_name': room_name
    })

def webinars(request): 
    if request.user.is_authenticated == False:
            return HttpResponseRedirect('/account/login')
   # web_send_mail("Ты")
    user = User.objects.get(username=request.user)  
    webinarsUser = user.ticketwebinar_set.all() 
    return render(request, 'LearnSystem/webinars.html', context= { 'webinars': webinarsUser })

def cource(request,pk): 
    if request.user.is_authenticated == False:
            return HttpResponseRedirect('/account/login')
    
    start_date = datetime(2021, 1, 11)
    end_date = start_date + relativedelta(days=2)
    
         
    stats = StatsCource.objects.all()
    values = []
    for x in stats:
        values.append([x.datetime,x.progressToDay])
    user = User.objects.get(username=request.user)   
    return render(request, 'LearnSystem/courceStats.html', {'values': values})