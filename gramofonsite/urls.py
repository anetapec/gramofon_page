from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'gramofonsite'
urlpatterns = [
    path('', views.gramofonsite_list, name='gramofonsite_list'), 
    path('morska/', views.morska, name='morska'),



    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



