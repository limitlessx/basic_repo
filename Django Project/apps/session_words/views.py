# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render (request,'session_words/index.html')

def process(request):
    if "store" not in request.session:
        request.session['store']=[]
    if request.method=="POST":
        word=request.POST['word']
        color=request.POST['color']
        if 'checkbox' in request.POST:
            font="big"
        else:
            font="normal"
        date=strftime("%H:%M %p, %b %d %Y", gmtime())

        data={
            "word":"{}".format(word),
            "color":"{}".format(color),
            "time":" - add on {}".format(date),
            'checkbox':"{}".format(font)
        }
        
        request.session['store'].append(data)
        print request.session['store']
        return redirect('/session_words')

def reset(request):
    request.session.clear()
    return redirect('/session_words')