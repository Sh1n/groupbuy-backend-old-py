from django.conf.urls import url, include
from api.views import OfferViewSet, UserViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns

offer_list = OfferViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
offer_detail = OfferViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^offers/$', offer_list, name='offer-list'),
    url(r'^offers/(?P<pk>[0-9]+)/$', offer_detail, name='offer-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])
