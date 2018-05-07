# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
#============================================================
#this is for first_app
# the index function is called when root is visited
def index(request):
    response = "this is a view for first_app"
    return HttpResponse(response)

def test(request):
    response = "i am test this is working"
    return HttpResponse(response)

