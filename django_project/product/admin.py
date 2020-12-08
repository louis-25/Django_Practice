from django.contrib import admin
from django.utils.html import format_html # 내가 입력한 html태그를 인식하게해줌
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Dj_Product

# Register your models here.

class Dj_Product_Admin(admin.ModelAdmin):
    list_display = ('name', 'price_format', 'styled_stock') # model에서 표시할 항목

    def price_format(self, obj):
        price = intcomma(obj.price)
        return f'{price} 원'

    def styled_stock(self, obj):
        stock = obj.stock
        if stock <= 50:
            stock = intcomma(stock)
            return format_html(f'<b><span style="color:red">{stock} 개</span></b>')        
        return format_html(f'<b>{intcomma(stock)}</b> 개')

    def changelist_view(self, request, extra_context=None): # 제목바꾸기
        extra_context = { 'title': '상품 목록' }
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None): # 수정페이지 제목변경
        product = Dj_Product.objects.get(pk=object_id)
        extra_context = {'title': f'{product.name} 수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)


    price_format.short_description='가격'
    styled_stock.short_description='재고'

admin.site.register(Dj_Product, Dj_Product_Admin)