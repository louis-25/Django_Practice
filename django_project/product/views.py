from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Dj_Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm


# Create your views here.

class ProductList(ListView):
    model = Dj_Product
    template_name = 'product.html'
    context_object_name = 'product_list' # product.hmtl에서 object_list대신 사용하고싶은 변수명

class ProductCreate(FormView):        
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url =  '/product/'

class ProductDetail(DetailView):        
    template_name = 'product_detail.html'
    queryset = Dj_Product.objects.all()
    context_object_name = 'product_detail'    

    def get_context_data(self, **kwargs): # 현재 페이지의 인자값을 전달하기위해 사용함
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request) # self.request로 현재 클래스의 정보를 넘긴다
        return context
    