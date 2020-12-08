from django.contrib import admin
from django.utils.html import format_html # 내가 입력한 html태그를 인식하게해줌
from .models import Dj_Order

# Register your models here.

class Dj_Order_Admin(admin.ModelAdmin):
    list_filter = ('status',) # 필터추가
    list_display = ('djuser', 'product', 'styled_status') # model에서 표시할 항목

    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html(f'<b><span style="color:red">{obj.status}</span></b>')
        if obj.status == '결제완료':
            return format_html(f'<b><span style="color:green">{obj.status}</span></b>')
        return format_html(f'<b>{obj.status}</b>')
    
    def changelist_view(self, request, extra_context=None): # 제목바꾸기
        extra_context = { 'title': '주문 목록' }
        return super().changelist_view(request, extra_context)
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None): # 수정페이지 제목변경
        order = Dj_Order.objects.get(pk=object_id)
        extra_context = {'title': f"'{order.djuser.email}'의 '{order.product.name}' 주문 수정하기'"}
        return super().changeform_view(request, object_id, form_url, extra_context)

    styled_status.short_description='상태' # 목록명 바꾸기

admin.site.register(Dj_Order, Dj_Order_Admin)