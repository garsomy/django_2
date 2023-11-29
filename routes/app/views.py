from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def main(request):
    return HttpResponsePermanentRedirect('faq')
    # return HttpResponse(f'<h1>Главная страница</h1>')


def news(request):
    return HttpResponseRedirect('shop/3/product')


def product(request, pk):
    return HttpResponse(f'<h1>Страница товаров № {pk}</h1>')


def cart(request, pk):
    name = request.GET.get('prod', 'Noname')
    color = request.GET.get('color')
    size = request.GET.get('size')
    price = request.GET.get('price')

    return HttpResponse(f'<h1>Корзина пользователя {pk}</h1> <p>Товар {name} </p>'
                        f'<p> Цвет {color}</p> <p> Цена {price} </p> Размер {size} </p>')


def order(request, pk):
    return HttpResponse(f'<h1>Мои заказы {pk}</h1>')


def faq(request):
    return HttpResponse(f'<h1>Ваши вопросы</h1>')