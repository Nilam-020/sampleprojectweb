from django.shortcuts import render
from .models import destinationdemo
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    dests = destinationdemo.objects.all()
    return render(request,'index.html',{'dests':dests})

def about(request):
    return render(request,'about.html')