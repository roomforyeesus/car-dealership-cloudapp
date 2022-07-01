from django.contrib import admin
# from .models import related models
from .models import CarDealer, CarMake, CarModel

# Register your models here.
class CarDealerAdmin(admin.ModelAdmin):
    list_display = ('full_name')
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_model')
class CarModelInLine(admin.StackedInline):
    model = CarModel
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInLine,]
    list_display = ('car_make')


# Register models here
