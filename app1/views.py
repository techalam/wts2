from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from app1.models import contactform, join2
# Create your views here.
def home(request):
    return render(request,'index.html', {'':'home'})

def ourchannels(request):
    return render(request,'ourchannels.html',{'channels':'channels'})

def ourvideos(request):
    return render(request,'ourvideos.html',{'videos':'videos'})

def contact(request):
    return render(request,'contactus.html',{'contact':'contact'})

def team(request):
    return render(request,'ourteam.html',{'ourteam':'ourteam'})

def website(request):
    return render(request,'website.html',{'datawebsite':'datawebsite'})

def contactus(request):
    
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact1=contactform(name=name, email=email, message=message, date=datetime.today())
        contact1.save()
    return render(request,'contactform.html',{'contactus':'contactus'})

def joinus(request):
    if request.method == "POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Message=request.POST.get('Message')
        Experience=request.POST.get('Experience')
        Cv=request.POST.get('Cv')
        Re=request.POST.get('Re')
        join1=join2(Name=Name, Email=Email, Message=Message, date=datetime.today(), Experience=Experience, Cv=Cv, Re=Re,)
        join1.save()
    return render(request,'joinus.html',{'joinus':'joinus'})

    