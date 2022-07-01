from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel


# Register your models here.

class CarModelAdmin(admin.ModelAdmin):
    fields=["car_make", "dealer_id", "name", "type", "year"]
class CarModelInline(admin.StackedInline):
    model=CarModel
    extra=3
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields=["name", "description"]
    inlines=[CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)