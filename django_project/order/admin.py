from django.contrib import admin
from .models import Dj_Order

# Register your models here.

class Dj_Order_Admin(admin.ModelAdmin):
    list_display = ('djuser', 'product') # model에서 표시할 항목

admin.site.register(Dj_Order, Dj_Order_Admin)