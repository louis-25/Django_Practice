import datetime
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType 
from django.db.models import F, Q
from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.html import format_html # 내가 입력한 html태그를 인식하게해줌
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.urls import path
from .models import Dj_Order

# Register your models here.
def refund(self, request, queryset):
    with transaction.atomic():
        qs = queryset.filter(~Q(status='환불')) # status가 환불이 아닌경우
        
        ct = ContentType.objects.get_for_model(qs.model) # 내가 지금 수정하는 모델이 어떤타입인지 알려줌
        for obj in qs:
            # if obj.status == '환불': continue
            obj.product.stock += obj.quantity
            obj.product.save()
            
            LogEntry.objects.log_action( # LogEntry는 무슨 모델을 수정하는지를 기록한다
                user_id=request.user.id,
                content_type_id=ct.pk,
                object_id=obj.pk,
                object_repr=f'{obj.product.name} 환불',
                action_flag=CHANGE,
                change_message='주문 환불'
            )
        qs.update(status='환불')
    

refund.short_description='환불'

class Dj_Order_Admin(admin.ModelAdmin):
    list_filter = ('status',) # 필터추가
    list_display = ('djuser', 'product', 'styled_status', 'action') # model에서 표시할 항목
    change_list_template = 'admin/order_change_list.html' # template 폴더를 지정할 수 있다    

    actions = [
        refund
    ]
    
    def action(self, obj):
        if obj.status != '환불':
            return format_html(f'<input type="button" value="환불" onclick="order_refund_submit({obj.id})" class="btn btn-primary btn-sm">')

    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html(f'<b><span style="color:red">{obj.status}</span></b>')
        if obj.status == '결제완료':
            return format_html(f'<b><span style="color:green">{obj.status}</span></b>')
        return format_html(f'<b>{obj.status}</b>')
    
    def changelist_view(self, request, extra_context=None): # 제목바꾸기
        extra_context = { 'title': '주문 목록' }

        if request.method == 'POST':            
            
            obj_id = request.POST.get('obj_id')
            if obj_id:
                qs = Dj_Order.objects.filter(pk=obj_id)
                ct = ContentType.objects.get_for_model(qs.model) # 내가 지금 수정하는 모델이 어떤타입인지 알려줌
                for obj in qs:
                    # if obj.status == '환불': continue
                    obj.product.stock += obj.quantity
                    obj.product.save()
                    
                    LogEntry.objects.log_action( # LogEntry는 무슨 모델을 수정하는지를 기록한다
                        user_id=request.user.id,
                        content_type_id=ct.pk,
                        object_id=obj.pk,
                        object_repr=f'{obj.product.name} 환불',
                        action_flag=CHANGE,
                        change_message='주문 환불'
                    )
                qs.update(status='환불')

        return super().changelist_view(request, extra_context)
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None): # 수정페이지 제목변경
        order = Dj_Order.objects.get(pk=object_id)
        # order = get_object_or_404(Dj_Order, pk=object_id)
        extra_context = {'title': f"'{order.djuser.email}'의 '{order.product.name}' 주문 수정하기'"}
        extra_context['show_save_and_add_another'] = False # 버튼 제거
        extra_context['show_save_and_continue'] = False # 버튼 제거
        return super().changeform_view(request, object_id, form_url, extra_context)

    def get_urls(self):
        urls = super().get_urls() # 기존의 url
        date_urls = [
            path('date_view/', self.date_view),
        ]
        return date_urls + urls
    
    def date_view(self, request):
        week_date = datetime.datetime.now() - datetime.timedelta(days=7)
        week_data = Dj_Order.objects.filter(register_date__gte=week_date)
        data = Dj_Order.objects.filter(register_date__lt=week_date)
        context = dict(
           self.admin_site.each_context(request), # 사이트의 기본적인 정보
           week_data = week_data,
           data = data
        )
        return TemplateResponse(request, 'admin/order_date_view.html', context)

    styled_status.short_description='상태' # 목록명 바꾸기

admin.site.register(Dj_Order, Dj_Order_Admin)