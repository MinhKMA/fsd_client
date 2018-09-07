from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'index.html')


def oke(request):
    if (request.GET.get('your_name')):
        name = request.GET.get('your_name')
        requests.post('http://127.0.0.1:8000/api/person/',
                      data={'name': name})
    return HttpResponse('Chuc mung ban, {}'.format(name))