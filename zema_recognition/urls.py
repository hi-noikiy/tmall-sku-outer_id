"""
Definition of urls for zema_recognition.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()
import app.views
import django.contrib.auth.views
urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r"^deal/$",app.views.deal,name="deal"),
    url(r'^commodity/all/$', app.views.about, name='commodity-all'),
    url(r"^sync/$",app.views.sync,name = "sync"),
    url(r"^commodity/detail/$",app.views.detail,name="detail"),
    url(r"clothe/all/$", app.views.clothe, name="clothe"),
    url(r"clothe/new/$", app.views.addclothe, name="addclothe"),
    url(r"show/img/$",app.views.show_img,name="show_img"),
    url(r"clothe/get/color/$",app.views.get_color,name="get_color"),
    url(r'^updata/$',app.views.updata,name="updata"),
    url(r"^detail/sku/$",app.views.detail_sku, name="detail_sku"),
    url(r'^commodity/3day/$',app.views.get_3day,name="get3day"),

    url(r"^register/$",app.views.register,name="register"),
    url(r"^clothe/change/$",app.views.addclothe,name="changeclothe"),




    url(r'^login/$',
        app.views.login,
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
