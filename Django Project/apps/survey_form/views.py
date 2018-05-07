# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render (request, "survey_form/index.html")

def surveys_process(request):
    if request.method=="POST":
        if 'count' not in request.session:
            request.session['count']=0
        request.session['name']=request.POST['name']
        request.session['location']=request.POST['location']
        request.session['lang']=request.POST['lang']
        request.session['desc']=request.POST['desc']
        request.session['count']=request.session['count']+1
        
        return redirect ('/survey_form/result')

def result(request):
    return render (request, "survey_form/result.html")

def reset(request):
    request.session.clear()
    return redirect ('/')

