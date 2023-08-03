from django.shortcuts import render
from .models import Local

def gramofonsite_list(request):
    locals = Local.objects.all()  # inquiry to database
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/gramofonsite_list.html', {'locals': locals})

def morska(request):
    morska_obj = Local.objects.get(id=2)  # inquiry to database
    context = {'locals': locals, 'morska_obj': morska_obj }
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/morska.html', context)

def bootstrap(request):
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/bootstrap.html')

def navigation(request):
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/navblock.html')

  
