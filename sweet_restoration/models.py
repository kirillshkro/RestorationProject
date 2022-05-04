from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topping(models.Model):
    title = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    description = models.TextField()
    image = models.ImageField(blank=False)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title


class Order(models.Model):
    topping = models.ForeignKey('Topping', on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True, null=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Phone(models.Model):
    phone = models.CharField(max_length=50, blank=False)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)

    def __str__(self):
        return self.phone


class Restaurant(models.Model):
    title = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=255, blank=False)
    time_opening = models.TimeField(blank=False)
    time_close = models.TimeField(blank=False)

    def __str__(self):
        return self.title
