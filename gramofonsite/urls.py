from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'gramofonsite'
urlpatterns = [
    path('gramofon-lokal', views.gramofonsite_list, name='gramofonsite_list'), 
    path('gramofon-morska/', views.morska, name='morska'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('navigation/', views.navigation, name='navigation'),
    path('grabowek/', views.grabowek, name='grabowek')
    
    #path('imprezy/', views.bootstrap, name='imprezy'),



    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



