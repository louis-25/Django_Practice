from django.db import models

# Create your models here.

class Dj_Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self): # 대표로 표시할 이름
        return self.name

    class Meta: # 관리자페이지
        db_table = 'dj_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'