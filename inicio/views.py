from django.contrib.sites import requests
from django.http import JsonResponse
from django.shortcuts import render
import requests


def index(request):
    return render(request, 'index.html')


def my_api_view(request):
    response = requests.get('https://exemplo.com/api/')
    data = response.json()
    return JsonResponse(data)
