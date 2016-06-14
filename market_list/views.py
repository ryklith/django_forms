from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import MarketListEntry, fill_default_market_list, add_market_entry
from .forms import CompetitionRequestForm


def get_context():
    list = MarketListEntry.objects.order_by('position')
    defaults = {'name': "Muenchner",
                'working_price': 50,
                'target_position': 0,
                'fallback_rule': 'SH',
                'working_price_reduction_interval': 0.01
                }
    form = CompetitionRequestForm(initial=defaults)
    context = {'list': list, 'form': form}
    return context


def index(request):
    return render(request, 'market_list/index.html', get_context())


def fill_market_list(request):
    fill_default_market_list()
    return HttpResponseRedirect(reverse('market_list:index'), get_context())


def submit_request(request):
    name = request.POST['name']
    price = request.POST['working_price']
    position = request.POST['target_position']
    add_market_entry(name, price, position)

    return HttpResponseRedirect(reverse('market_list:index'), get_context())

