from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import InsuranceQuote, fill_default_market_list, process_competition_request
from .forms import CompetitionRequestForm


def get_context():
    list = InsuranceQuote.objects.order_by('price')
    defaults = {'name': "Muenchner",
                'working_price': 50,
                'target_position': 0,
                'fallback_rule': 'SH',
                'working_price_reduction_interval': 0.01,
                'max_working_price_reduction': 10
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
    if request.method == 'POST':
        form = CompetitionRequestForm(request.POST)
        if form.is_valid():
            process_competition_request(form.instance)

    return HttpResponseRedirect(reverse('market_list:index'), get_context())


