from django.urls import path
from . import views

urlpatterns = [
    path('', views.gramofonsite_list, name='gramofonsite_list'), 
]
