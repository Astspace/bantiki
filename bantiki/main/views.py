from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = ['Обо мне', 'Работы', 'Контакты']
bants = [
    {'id': 1, 'name': 'Бант № 1', 'color': 'Красный'},
    {'id': 2, 'name': 'Бант № 2', 'color': 'Синий'},
    {'id': 3, 'name': 'Бант № 3', 'color': 'Фиолетовый'}
]
def index(request): #HttpReqest
    data = {'tittle': 'Заголовочек', 'menu': menu, 'bants': bants}
    return render(request, 'main/index.html', context=data)

def categories(request, cat_id):
    if cat_id > 100:
        return redirect('home')
    return HttpResponse(f"Страница категорий, cat_id = {cat_id}")

def years(request, year):
    return HttpResponse(f"Тест прошел удачно, год: {year}")

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена!")