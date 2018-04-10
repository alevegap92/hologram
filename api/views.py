from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
# Create your views here.

class HologramFilter(filters.FilterSet):
    class Meta:
        model = Hologram
        fields = ['name', 'to_update']

class HologramViewSet(viewsets.ModelViewSet):
    queryset = Hologram.objects.all()
    serializer_class = HologramSerializer
    filter_class = HologramFilter