from django.shortcuts import render
from .models import *
def Wp(request):
    return render(request,'home.html')

# Create your views here.
