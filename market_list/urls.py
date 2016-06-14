from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fill/', views.fill_market_list, name='fill_market_list'),
    url(r'^submit/', views.submit_request, name='submit_request')
]
