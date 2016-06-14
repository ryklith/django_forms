from django.http import HttpResponse
from django.shortcuts import render

from .models import MarketListEntry, fill_default_market_list


def index(request):
    list = MarketListEntry.objects.order_by('position')
    context = {'list': list}
    return render(request, 'market_list/index.html', context)


def fill_market_list(request):
    fill_default_market_list()
    return index(request)

