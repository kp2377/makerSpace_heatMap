from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.charts, name='charts'),
    url(r'^json', views.json, name='charts'),
]