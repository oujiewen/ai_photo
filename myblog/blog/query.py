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
    query_eid=request.POST.get('eid','')
    query_name = request.POST.get('name', '')
    query_limit = request.POST.get('limit', '')
    query_status = request.POST.get('status', '')
    query_address = request.POST.get('address', '')
    if request.method=='POST':
        if query_eid!='' or query_name!='' or query_limit!='' or query_status!='' or query_address!='':
            filter={}
            if query_eid:
                filter['id'] = query_eid
            if query_name:
                filter['name__contains'] = query_name
            if query_limit:
                filter['limit'] = query_limit
            if query_status:
                filter['status'] = query_status
            if query_address:
                filter['address__contains'] = query_address
            print filter
            try:
                result=Event.objects.filter(**filter)
                p=result.count()
            except ObjectDoesNotExist:
                return JsonResponse({'STATUS': -3, 'message': '查询异常'},json_dumps_params={'ensure_ascii': False})
            if p!=0:
                list=[]
                for x in result:
                    event = {}
                    event['eid'] = x.id
                    event['name'] = x.name
                    event['limit'] = x.limit
                    event['status'] = x.status
                    event['address'] = x.address
                    event['start_time'] = x.start_time
                    event['create_time'] = x.create_time
                    list.append(event)
                return JsonResponse({'total':p,'STATUS': 1, 'message': '查询成功','date':list}, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({'STATUS': -1, 'message': '查询无结果'}, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'STATUS': -1, 'message': '查询条件不能为空'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'STATUS': -2, 'message': '非法访问'}, json_dumps_params={'ensure_ascii': False})