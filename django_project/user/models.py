from django.db import models

# Create your models here.

class Dj_User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta: # 관리자페이지
        db_table = 'dj_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'