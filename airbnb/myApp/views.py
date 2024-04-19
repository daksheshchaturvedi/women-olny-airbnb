from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'header': "HOME"} ) 

def login(request):
    return render(request,'login.html',{'Header': "LOGIN"} )