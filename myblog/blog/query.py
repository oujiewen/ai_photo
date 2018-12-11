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


def deal_query_set(result):  #处理查询set[]转化成一个list，并return
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
    return list

def query_event(request):
    parmes=request.POST
    list=['eid','name','limit''status','address','start_time_begin,''start_time_end']
    print parmes
    for key in parmes:
        if key not in list:
            return JsonResponse({'STATUS': -1, 'message': '不合法字段'}, json_dumps_params={'ensure_ascii': False})
            break
    query_eid=request.POST.get('eid','')     #从requset获取查询的值
    query_name = request.POST.get('name', '')
    query_limit = request.POST.get('limit', '')
    query_status = request.POST.get('status', '')
    query_address = request.POST.get('address', '')
    query_start_time_begin=request.POST.get('start_time_begin')
    query_start_time_end=request.POST.get('start_time_end')
    if request.method=='POST':     #判断调用的方法
        print "----in post----"
        if query_eid or query_name or query_limit or query_status or query_address or query_start_time_begin or query_start_time_end: #判断是否传了查询参数
            print "----in filter----"
            filter={}      #添加filter参数
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
            if query_start_time_begin and query_start_time_end:
                list=[query_start_time_begin,query_start_time_end]
                filter['start_time__range'] = list
            else:
                if query_start_time_begin:
                    filter['start_time__gte'] = query_start_time_begin
                if  query_start_time_end:
                    filter['start_time__lte'] = query_start_time_end
            try:
                print "----in query----"
                result=Event.objects.filter(**filter) #根据filter查询
                print filter
                p=result.count() #获取查询数据的条数
            except ObjectDoesNotExist, Argument:
                print Argument
            if p!=0: #如果数据大于0条
                list=deal_query_set(result)
                return JsonResponse({'total':p,'STATUS': 1, 'message': '查询成功','date':list}, json_dumps_params={'ensure_ascii': False})# 数据条数大于0返回条数和list
            else:
                return JsonResponse({'STATUS': -1, 'message': '查询无结果'}, json_dumps_params={'ensure_ascii': False})#数据条数等于0，返回无结果
        else:
            if request.POST:
                return JsonResponse({'STATUS': -1, 'message': '不合法字段'}, json_dumps_params={'ensure_ascii': False})
            else:
                result=Event.objects.all()
                p=result.count()
                list=deal_query_set(result)
                return JsonResponse({'total':p,'STATUS': 1, 'message': '查询成功','date':list}, json_dumps_params={'ensure_ascii': False})# 数据条数大于0返回条数和list
    else:

        return JsonResponse({'STATUS': -2, 'message': '非法访问'}, json_dumps_params={'ensure_ascii': False})#提交方式部位post，返回非法访问