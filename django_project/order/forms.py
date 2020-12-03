from django import forms
from .models import Dj_Order

class RegisterForm(forms.Form):
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
        