from django.shortcuts import render
from .models import Destination
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def new (request):
    dest1= Destination()
    dest1.username='User name'
    dest1.password='Password'
    return render(request,"new 1.html",{'dest1': dest1})
