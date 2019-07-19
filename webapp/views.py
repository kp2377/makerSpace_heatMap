from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>This is kartikey purohit in webapp</h2>")
