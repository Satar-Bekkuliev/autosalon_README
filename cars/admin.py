from django.contrib import admin
from .models import Car, CarBrand, CarBodyType, Dealer

admin.site.register(Car)
admin.site.register(CarBodyType)
admin.site.register(CarBrand)
admin.site.register(Dealer)