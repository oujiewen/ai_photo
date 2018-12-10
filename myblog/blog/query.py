# -*-coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from blog.models import Event
from django.http import JsonResponse
import json

def query_event(request):
    eid=request.POST.get('eid','')
    name=request.POST.get('name','')
    if request.method=="GET":
        return  JsonResponse({'status':-1,'message':'非法访问'},json_dumps_params={'ensure_ascii':False})
    if id !='':
        event={}
        try:
            q1=Event.objects.get(id=eid)
            print q1.start_time
        except ObjectDoesNotExist:
            return  JsonResponse({'status':-1,'message':'id不存在'},json_dumps_params={'ensure_ascii':False})
        else:
            event['name']=q1.name
            event['limit']=q1.limit
            event['status']=q1.status
            event['address']=q1.address
            event['start_time']=q1.start_time
            return JsonResponse({'status':1,'message':'查询成功','date':event},json_dumps_params={'ensure_ascii':False})

    else:
         return  JsonResponse({'status':-1,'message':'id不能为空'},json_dumps_params={'ensure_ascii':False})
