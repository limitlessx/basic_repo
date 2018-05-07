# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from  django.utils.crypto import get_random_string 


# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    return render (request,'random_word/index.html')

def generate(request):
    unique_id = get_random_string(length=14)
    if 'word' not in request.session:
        request.session['word']=[]
    
    request.session['word'] = unique_id
    request.session['count']=request.session['count']+1
    return redirect ('/random_word')

def reset(request):
    request.session.clear()
    return redirect ('/random_word')