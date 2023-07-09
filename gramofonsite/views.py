from django.shortcuts import render
from .models import Local

def gramofonsite_list(request):
    locals = Local.objects.all()  # inquiry to database
    return render(request, 'gramofonsite_list.html', {'locals': locals})
 