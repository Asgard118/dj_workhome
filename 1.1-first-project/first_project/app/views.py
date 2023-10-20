from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import os
import datetime

def home_view(request):
    template_name = 'app/home.html'

    # Используем reverse для получения адресов страниц
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_time_view(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    workdir_content = os.listdir('.')
    msg = f'Содержимое рабочей директории: {workdir_content}'
    return HttpResponse(msg)
