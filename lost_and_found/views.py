# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lost_and_found import models
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect,Http404


def find(request):
    return render_to_response('find.html')


def index(request):
    return render_to_response('index.html')

def Login(request):
    return render_to_response('Login.html')

def tests(request):
        return render_to_response('tests.html')


 #插入函数
def insert(request):
    if request.method == "POST":
        #iform = request.POST
        #if iform.is_valid():
         #   cd = iform.cleaned_data
        #thingname = iform.thingname,
        #find_place=iform.find_place,
        #find_date = iform['find_date'],
        #discription= iform['discription'],
        #contact = iform['contact'],

        thingname = request.POST.get("thingname", None)
        find_place = request.POST.get("find_place", None)
        find_date = request.POST.get("find_date", None)
        description = request.POST.get("description", None)
    #    announcer = request.POST.get("announcer", None)
        contact = request.POST.get("contact", None)

        models.thing.objects.create(
            thingname=thingname,
            contact=contact,
            find_place=find_place,
            find_date=find_date,
            description = description,)


        thing_list=models.thing.objects.all()

    #return render(request, 'seethings.html',{'thingname':thingname,'find_place':find_place})
    return render(request, 'seethings.html', {"thing_list":thing_list})
    #return HttpResponse(' thingname=' +  thingname + "&find_place=" +find_place+  \
    #                                                                   '&find_date=' +   find_date + "&discription=" + discription+ '&contact=' +  contact )



def see(request):
    thing_list = models.thing.objects.all()
    return render(request, 'seethings.html', {"thing_list":thing_list})


def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    raise Http404

def some_page_get(request):
    assert request.method == 'GET'
    return render_to_response('index.html')

