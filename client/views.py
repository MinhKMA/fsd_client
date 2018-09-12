from django.shortcuts import render
from django.http import HttpResponse
import requests
import os 


def index(request):
    return render(request, 'index.html')


def oke(request):
    if (request.GET.get('your_name')):
        name = request.GET.get('your_name')
        requests.post('http://{}/api/person/'.format(os.environ['SERVER_IP']),
                      data={'name': name})
    return HttpResponse('Chuc mung ban, {}'.format(name))
