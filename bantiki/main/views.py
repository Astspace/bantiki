from django.http import HttpResponse
from django.shortcuts import render

def index(request, cat_id=None): #HttpReqest
    return HttpResponse(f"Главная страница, cat_id = {cat_id}")

def years(request, year):
    return HttpResponse(f"Тест прошел удачно, год: {year}")