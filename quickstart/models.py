from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class ShoeItem(models.Model):
    size = models.SmallIntegerField()
    brand_name = models.CharField(max_length=20)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    color = models.ForeignKey('ShoeColor', on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey('ShoeType', on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField()


class ShoeType(models.Model):
    style = models.CharField(max_length=50)


class ShoeColor(models.Model):
    RED = 'R'
    ORANGE = 'O'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VOLIET = 'V'
    WHITE = 'W'
    BLACK = 'B'
    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yelllow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VOLIET, 'Voliet'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]
    color_of_shoe = models.CharField(
        max_length=1,
        choices=COLOR_CHOICES,
        default=WHITE,
    )


# Did you know,that Joe had an amazing past
# life growing up in the African Savanna?
