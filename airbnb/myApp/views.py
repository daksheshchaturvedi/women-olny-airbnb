from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Provider, Renter

def index(request):
    return render(request, 'index.html', {'header': "HOME"} ) 


def renter_login(request):
    return render(request,'renter-login.html',{'Header': "R_LOGIN"} )


def provider_login(request):
    return render(request,'provider-login.html',{'HEADER': "P_LOGIN"})



def renter_form(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mail = request.POST.get('mail')
        age = request.POST.get('age')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')
        req_occupancy = request.POST.get('req_occupancy')
        gender = request.POST.get('gender')

        renter = Renter.objects.create(
            fname=fname,
            lname=lname,
            mail=mail,
            age=age,
            city=city,
            mobile=mobile,
            req_occupancy=req_occupancy,
            gender=gender
        )
        renter.save()

        messages.success(request, 'Login successfully and redirect to home page')
        return redirect('export/')
    else:
        return render(request, 'not_found')


def provider_form(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mail = request.POST.get('mail')
        age = request.POST.get('age')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')
        req_occupancy = request.POST.get('req_occupancy')
        gender = request.POST.get('gender')

        provider = Provider.objects.create(
            fname=fname,
            lname=lname,
            mail=mail,
            age=age,
            city=city,
            mobile=mobile,
            req_occupancy=req_occupancy,
            gender=gender
        )
        provider.save()

        messages.success(request, 'Login successfully and redirect to home page')
        return redirect('export/')
    else:
        return render(request, 'notfound')



def your_view(request):
    providers = Provider.objects.all()
    renters = Renter.objects.all()
    return render(request, 'matches.html', {'providers': providers, 'renters': renters})


