from django.db import models

# Create your models here.

class Dj_User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    level = models.CharField(max_length=8, verbose_name='등급',
        choices=(
            ('admin', 'admin'),
            ('user', 'user'),                        
        ),
        null=True)
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self): # 대표로 표시할 이름
        return self.email

    class Meta: # 관리자페이지
        db_table = 'Dj_User'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'