from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') # Fcuser를 눌러서 들어갔을때 보여줄 속성명


admin.site.register(Fcuser, FcuserAdmin) # 등록
