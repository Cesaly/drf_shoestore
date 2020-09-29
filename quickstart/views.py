# from django.shortcuts import render
from quickstart.models import ShoeItem, Manufacturer, ShoeType, ShoeColor
from rest_framework import viewsets
from quickstart.serializers import (ShoeItemSerializer, ManufacturerSerializer,
                                    ShoeColorSerializer, ShoeTypeSerializer)
# Create your views here.


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeItemViewSet(viewsets.ModelViewSet):
    queryset = ShoeItem.objects.all()
    serializer_class = ShoeItemSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer
