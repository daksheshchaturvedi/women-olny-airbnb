from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

def index(request):
    context={}
    return render(request, 'index.html', {'header': "HOME"} ) 

