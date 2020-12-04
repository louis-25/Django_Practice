from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from user.decorators import login_required
from django.db import transaction # 트랜잭션
from .forms import RegisterForm
from .models import Dj_Order
from product.models import Dj_Product
from user.models import Dj_User
# Create your views here.

@method_decorator(login_required, name='dispatch') # decorator
class OrderCreate(FormView):            
    form_class = RegisterForm
    success_url =  '/product/'

    def form_valid(self, form):
        with transaction.atomic(): # with안에있는 내용을 기반으로 트랜잭션 처리
                prod = Dj_Product.objects.get(pk=form.data.get('product'))
                order = Dj_Order(
                    quantity=form.data.get('quantity'),
                    product=prod,
                    djuser=Dj_User.objects.get(email=self.request.session.get('user'))
                )
                order.save()
                prod.stock -= int(form.data.get('quantity'))
                prod.save()
        return super().form_valid(form)
    
    def form_invalid(self, form): # 에러가 발생했을때
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs): # form을 생성할때 어떤 인자값을 전달해줄지 결정해주는 함수
        kw = super().get_form_kwargs(**kwargs) # kw에는 FormView가 기본적으로 생성하는 인자값들이 들어간다
        kw.update({
            'request':self.request # request인자값 추가
        })
        return kw

@method_decorator(login_required, name='dispatch') # decorator
class OrderList(ListView):
    model = Dj_Order
    template_name = 'order.html'
    context_object_name = 'order_list' # order.hmtl에서 object_list대신 사용하고싶은 변수명

    def get_queryset(self, **kwargs): # 현재 로그인한 사용자의 주문정보만 조회 가능하게 함
        queryset = Dj_Order.objects.filter(djuser__email=self.request.session.get('user'))
        return queryset
        