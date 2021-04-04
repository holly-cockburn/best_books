from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context_dict ={'boldmessage':'boooooooooooooo'}
    return render(request, 'books/home.html', context_dict)

def about (request):
    context_dict ={}
    return render(request,'books/about.html', context_dict)
