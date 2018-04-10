from rest_framework import renderers
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from hologram import views
from api.views import Hologram
  
hologram_list = HologramViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
hologram_detail = HologramViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^list/$', hologram_list, name='hologram-list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', hologram_detail, name='hologram-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)