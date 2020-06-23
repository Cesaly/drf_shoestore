from django.contrib.auth.models import User
from tutorial.quickstart.models import ShoeItem, Manufacturer
from rest_framework import serializers


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'website'
        ]


class ShoeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeItem
        fields = [
            'size',
            'brand name',
            'manufacturer',
            'color',
            'material',
            'shoe type',
            'fasten type'
        ]
