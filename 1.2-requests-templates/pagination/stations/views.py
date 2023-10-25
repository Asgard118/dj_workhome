from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        bus_stations_data = list(reader)

    page = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations_data, 14)
    this_page = paginator.get_page(page)

    context = {
        'bus_stations': this_page.object_list,
        'page': this_page
    }
    return render(request, 'stations/index.html', context)
