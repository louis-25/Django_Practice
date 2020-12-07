from django.db import models

# Create your models here.

class Dj_Order(models.Model):
    djuser = models.ForeignKey('user.Dj_User', on_delete=models.CASCADE, verbose_name='사용자') # user의 Dj_User class를 참조
    product = models.ForeignKey('product.Dj_Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    status = models.CharField(
        choices=(
            ('대기중', '대기중'),
            ('결재대기중', '결재대기'),
            ('결제완료', '결제완료'),
            ('환불', '환불'),
        ),
        default='대기중', max_length=32, verbose_name='상태')
    memo = models.TextField(null=True, blank=True, verbose_name='메모')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    
    def __str__(self): # 대표로 표시할 이름
        return str(self.djuser) + ' ' + str(self.product)

    class Meta: # 관리자페이지
        db_table = 'Dj_Order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
    