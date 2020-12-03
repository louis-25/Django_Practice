from django.shortcuts import render
from django.views.generic import ListView
from .models import Dj_Product

# Create your views here.

class ProductList(ListView):
    model = Dj_Product
    template_name = 'product.html'
    context_object_name = 'product_list' # product.hmtl에서 object_list대신 사용하고싶은 변수명