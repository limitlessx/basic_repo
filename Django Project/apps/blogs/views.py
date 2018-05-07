from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
#============================================================
#this is for blogs
  # the index function is called when root is visited
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "blogs/index.html", context)

def new(request):
    response = "thi is a new page for blogs"
    return HttpResponse(response)

def show_digit(request,number):
    response = "<h1> This is page {} - digital page</h1>".format(number)
    return HttpResponse(response)

def edit(request,number):
    response = " <h1> editing page {}  - digital page </h1>".format(number)
    return HttpResponse(response)

def delete(request,number):
    response = "<h1> Here to delete page {}- digital page</h1> ".format(number)
    return redirect ('/')