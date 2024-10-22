from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = [
    {'title': 'Обо мне', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contacts'}
]
db_bnts = [
    {'id': 1, 'name': 'Бант № 1', 'color': 'Красный', 'is_published': True},
    {'id': 2, 'name': 'Бант № 2', 'color': 'Синий', 'is_published': True},
    {'id': 3, 'name': 'Бант № 3', 'color': 'Фиолетовый', 'is_published': True}
]
def index(request): #HttpReqest
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'bnts': db_bnts
    }
    return render(request, 'main/index.html', context=data)

def about(request):
    data = {
        'title': 'Обо мне',
        'txt': 'Привет! Меня зовут Анна и я - мастер по изготовлению бантов. Со стажем!',
        'menu': menu
    }
    return render(request, 'main/about.html', context=data)

def bnts(request, bnt_id):
    bnt_idx = 0
    for i, j in enumerate(db_bnts):
        if j['id'] == bnt_id:
            bnt_idx = i

    data = {
        'title': 'Просмотр бантов',
        'menu': menu,
        'bnt': db_bnts[bnt_idx]
    }
    return render(request, 'main/bnt.html', context=data)

def contacts(request):
    data = {
        'title': 'Контакты',
        'link': {'vk': 'ссылка на группу вк', 'tg': 'ссылка на канал тг'},
        'menu': menu
    }
    return render(request, 'main/contacts.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена!")