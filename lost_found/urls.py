"""lost_found URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from lost_and_found import views, models
from django.conf.urls import *
from django.views.generic import RedirectView



urlpatterns = patterns('lost_and_found.views',
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'see'),
    (r'^home/$', 'index'),
    url(r'^see/$', 'insert'),
    #url(r'^find/$', 'method_splitter', {'GET': 'some_page_get', 'POST': 'find'}),
    url(r'^find/$','find'),
    url(r'^seethings/$', 'see'),
    #url(r'^contact/$', 'lost_and_found.contact.contact', name='contact'),

    url(r'^detailed/$', 'detail'),
    url(r'^ChangeToFound/$','ChangeToFound'),
    url(r'^Addinfo/$','Addinfo'),

    url(r'^Login/$','Login'),
    url(r'^Create_success/$','C_success'),
    url(r'^Create_fail/$','C_fail'),
    url(r'^CreateUser/$','CreateUser'),

    url(r'^mythings/$', 'mythings'),
    #url(r'^mythings/$', views.mythings),
    (r'^find/$', RedirectView.as_view(url='/home/')),
    url(r'^tests/$', 'tests'),                  )




urlpatterns += patterns('lost_and_found.contact',
    (r'^contact/$', 'contact'),
)





