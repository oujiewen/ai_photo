#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog.models import Event,Guest

# Create your views here.
def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
        #if username=="admin" and password=="123456":
            auth.login(request,user)
            response=HttpResponseRedirect('/blog/success_login/')
            #response.set_cookie('user',username,3600)
            request.session['user']=username
            return response
        else:
            return render(request,"index.html",{'error':"username or password error!"})
    else:
        return render(request, "index.html", {'error': "please use post mothod!"})


@login_required
def success_login(request):
    #username=request.COOKIES.get('user','')
    event_list=Event.objects.all()
    #print event_list
    username=request.session.get('user','')
    #if username !="":
    return render(request,'success.html',{'user':username,'events':event_list})
    #else:
     # return render(request,"index.html",{'error':"please sgin in first!"})
