from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'gramofonsite'
urlpatterns = [
    path('', views.index, name='index'), 
    path('gramofon-lokal', views.gramofonsite_list, name='gramofonsite_list'), 
    path('gramofon-morska/', views.morska, name='morska'),
    path('gramofon-grabowek/', views.grabowek, name='grabowek'),
    path('gramofon-chylonia/', views.chylonia, name='chylonia'),
    path('regulamin/', views.statute, name='regulamin'),
    path('contact/', views.contact, name='contact'),
    path('imprezy-cateringowe/', views.catering, name='imprezy-cateringowe'),
    path('test/', views.test, name='test'),
    path('template', views.template, name='template'),
    path('templateG', views.templateG, name='templateG'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



