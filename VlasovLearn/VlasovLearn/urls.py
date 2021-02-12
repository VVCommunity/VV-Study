"""
Definition of urls for VlasovLearn.
"""

from django.urls import path,re_path, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
import os
from LearnSystem import views 
  
urlpatterns = [  
    path('', include('LearnSystem.urls')),
    path('blog/',include('BlogSystem.urls')),        
    path('accounts/',include('Accaunt.urls')),   
    path('', include('social_django.urls')), 
    path('admin/', admin.site.urls),  
    re_path('djga/', include('google_analytics.urls')),
    path('tap/', include('TapLinkByVlasov.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 