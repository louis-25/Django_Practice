from django.contrib import admin
from .models import Dj_User

# Register your models here.

class Dj_User_Admin(admin.ModelAdmin):
    list_display = ('email', ) # ,는 꼭 써줘야 튜플로 인식됨

admin.site.register(Dj_User, Dj_User_Admin) # admin에 model을 등록
admin.site.site_header="장고 백오피스"
admin.site.index_title="장고 인덱스"
admin.site.site_title="타이틀"