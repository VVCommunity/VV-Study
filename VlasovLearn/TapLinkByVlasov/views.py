from django.shortcuts import render
from .models import *
from django.http import Http404,HttpResponseRedirect,HttpResponsePermanentRedirect,HttpResponse

# Create your views here.

def tap(request, pk): 
    user = User.objects.get(username=pk) 
    taplink = user.taplink;
    
        
    buttons = taplink.tapbutton_set.all()
    return render(request, 'TapLinkByVlasov/index.html', context= { 'user':user,'buttons': buttons})
