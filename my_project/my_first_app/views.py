from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.
def hello_world(request, name):
    response = HttpResponse(f'<h1>Hello, {name}!</h1>')
    response.set_cookie('username', name)
    return response

def redirect_example(request):
    return redirect('hello_world', name='DefaultUser')

def json_example(request):
    data={'name':'John','age': 25}
    return JsonResponse(data)
def show_cookie(request):
    cookies = request.COOKIES
    return HttpResponse(f'<h1>Cookies: {cookies}</h1>')
