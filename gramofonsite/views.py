from django.shortcuts import render, redirect
from .models import Local


def index(request):
    return redirect('/gramofon-lokal')
    
def gramofonsite_list(request):
    locals = Local.objects.all()  # inquiry to database
    return render(request, 'gramofonsite_list.html', {'locals': locals})

def morska(request):
    morska_obj = Local.objects.get(id=2)  # inquiry to database
    context = {'locals': locals, 'morska_obj': morska_obj }
    return render(request, 'morska.html', context)

def grabowek(request):
    grabowek_obj = Local.objects.get(id=1)  # inquiry to database
    context = {'locals': locals, 'grabowek_obj': grabowek_obj}
    return render(request, 'grabowek.html', context) 

def chylonia(request):
    chylonia_obj = Local.objects.get(id=3)  # inquiry to database
    context = {'locals': locals, 'chylonia_obj': chylonia_obj}
    return render(request, 'chylonia.html', context) 

def contact(request):
    return render(request, 'contact.html')


def statute(request):
    return render(request, 'statute.html')

def test(request):
    return render(request, 'test.html')

