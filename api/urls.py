from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^offers/$', views.offer_list),
    url(r'^offers/(?P<pk>[0-9]+)/$', views.offer_detail),
]