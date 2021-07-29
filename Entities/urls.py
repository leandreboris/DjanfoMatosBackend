from django.conf.urls import url
from Entities import views

urlpatterns = [
    url(r'^clients/$', views.clientApi),
    url(r'^clients/([0-9]+)$', views.clientApi),
    url(r'^administrateurs/$', views.administrateurApi),
    url(r'^administrateurs/([0-9]+)$', views.administrateurApi),
]