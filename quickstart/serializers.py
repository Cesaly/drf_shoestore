from django.contrib.auth.models import User
from quickstart.models import ShoeItem, Manufacturer, ShoeType, ShoeColor
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
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]


class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            'style'
        ]


class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'color_of_shoe',
        ]