from django.contrib import admin
from .models import Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',) # 보여줄 속성


admin.site.register(Tag, TagAdmin) # 등록
