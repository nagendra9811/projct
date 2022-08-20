from django.shortcuts import render
from django.http import HttpResponse
from app.models import Department, Role, Employee
import json
def index(request):

    return render(request,'temp1.html')

def home(request):

    return render(request, 'temp.html')

def add(request):
    var1 = request.GET['num1']
    var2 = request.GET['num2']
    res = var1+var2
    return render(request, 'temp.html', {'result': res})
def fun(request):
    id = request.GET['id']
    obj = Department.objects.filter(id='id').values()
    return HttpResponse(obj)



