from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.management, name='management'),
    url(r'^$', views.current),
]