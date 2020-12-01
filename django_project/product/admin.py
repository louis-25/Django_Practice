from django.contrib import admin
from .models import Dj_Product

# Register your models here.

class Dj_Product_Admin(admin.ModelAdmin):
    list_display = ('name', 'price') # model에서 표시할 항목

admin.site.register(Dj_Product, Dj_Product_Admin)