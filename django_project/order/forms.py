from django import forms
from .models import Dj_Order
from product.models import Dj_Product # product폴더 models에 있는 Dj_Product
from user.models import Dj_User
from django.db import transaction

class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs): # 객체 생성됐을때 제일먼저 실행
        super().__init__(*args, **kwargs)
        self.request = request        
    
    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요'
        },
        label='수량'
    )    
    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요'
        },
        label='상품설명', widget=forms.HiddenInput # 사용자에게 보여지지않음
    )    

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')                

        if not (quantity and product):                        
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')            