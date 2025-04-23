from django.contrib import admin
from carr.models import Car 
from carr.models import Brand

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand', 'factory_year', 'model_year', 'value')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
