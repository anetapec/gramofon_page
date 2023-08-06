from django.shortcuts import render
from .models import Local
from .calendar_API import test_calendar

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

def grabowek(request):
    grabowek_obj = Local.objects.get(id=1)  # inquiry to database
    context = {'locals': locals, 'grabowek_obj': grabowek_obj}
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/grabowek.html', context) 

def chylonia(request):
    chylonia_obj = Local.objects.get(id=3)  # inquiry to database
    context = {'locals': locals, 'chylonia_obj': chylonia_obj}
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/chylonia.html', context) 

def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/demo.html', context)

def timetable(request):
    return render(request, '/home/aneta/software/repos/gramofon/gramofon_page/gramofonsite/templates/site/gramofon/home.html')
