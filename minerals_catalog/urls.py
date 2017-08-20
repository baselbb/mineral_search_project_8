"""minerals_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from . import views

urlpatterns = [
    url(r'search/$', views.mineral_search, name='search'),
    url(r'group/(?P<group>[a-zA-Z\s]{2,})/$', views.mineral_group, name='group'),
    url(r'letter/(?P<letter>[a-zA-Z])/$', views.mineral_letter, name='letter'),
    url(r'color/(?P<color>[a-zA-Z]+)/$', views.mineral_color, name='color'),
    url(r'^minerals/', include('minerals.urls', namespace='minerals')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns =[
         url(r'^__debug__/', include(debug_toolbar.urls)),
         ] + urlpatterns
