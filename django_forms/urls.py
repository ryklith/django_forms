from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_forms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^market_list/', include('market_list.urls', namespace='market_list')),
    url(r'^admin/', include(admin.site.urls)),
]
