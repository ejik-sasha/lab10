from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def nested_view1(request):
    return HttpResponse('<h1>Nested View 1</h1>')

def nested_view2(request):
    return HttpResponse('<h1>Nested View 2</h1>')