from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Dj_Order

# Create your views here.

class OrderCreate(FormView):            
    form_class = RegisterForm
    success_url =  '/product/'

    def form_invalid(self, form): # 에러가 발생했을때
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs): # form을 생성할때 어떤 인자값을 전달해줄지 결정해주는 함수
        kw = super().get_form_kwargs(**kwargs) # kw에는 FormView가 기본적으로 생성하는 인자값들이 들어간다
        kw.update({
            'request':self.request # request인자값 추가
        })
        return kw

class OrderList(ListView):
    model = Dj_Order
    template_name = 'order.html'
    context_object_name = 'order_list' # order.hmtl에서 object_list대신 사용하고싶은 변수명

    def get_queryset(self, **kwargs): # 현재 로그인한 사용자의 주문정보만 조회 가능하게 함
        queryset = Dj_Order.objects.filter(djuser__email=self.request.session.get('user'))
        return queryset