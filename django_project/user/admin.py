from django.contrib import admin
from .models import Dj_User

# Register your models here.

class Dj_User_Admin(admin.ModelAdmin):
    list_display = ('email', ) # ,는 꼭 써줘야 튜플로 인식됨
    
    def changelist_view(self, request, extra_context=None): # 제목바꾸기
        extra_context = { 'title': '사용자 목록' }
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None): # 수정페이지 제목변경
        user = Dj_User.objects.get(pk=object_id)
        extra_context = {'title': f'{user.email} 수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(Dj_User, Dj_User_Admin) # admin에 model을 등록
admin.site.site_header="장고 백오피스"
admin.site.index_title="장고 인덱스"
admin.site.site_title="타이틀"