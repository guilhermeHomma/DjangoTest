from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees

# Create your views here.
def index(request):
    list = Employees.objects.all()
    context = {
        'table': list
    }
    return render(request, 'index.html', context)