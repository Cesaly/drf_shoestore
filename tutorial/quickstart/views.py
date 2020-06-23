from django.shortcuts import render
from tutorial.quickstart.models import ShoeItem, Manufacturer
from rest_framework import viewsets
from tutorial.quickstart.serializers import ShoeItemSerializer, ManufacturerSerializer
# Create your views here.


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeItemViewSet(viewsets.ModelViewSet):
    queryset = ShoeItem.objects.all()
    serializer_class = ShoeItemSerializer
