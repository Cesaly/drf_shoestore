from django.core.management.base import BaseCommand
from quickstart.models import ShoeType, ShoeColor


class Command(BaseCommand):
    def handle(self, *args, **options):
        ShoeTypeList = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other']
        for Type in ShoeTypeList:
            ShoeType.objects.create(
                style=Type,
            )
        ShoeColorList = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black']
        for color in ShoeColorList:
            ShoeColor.objects.create(
                color_of_shoe=color,
            )
