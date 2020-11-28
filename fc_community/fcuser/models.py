from django.db import models

# Create your models here.

# DB스키마
class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    resistered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')
    
    def __str__(self): #Fcuser를 웹상에서 표시하는 함수
        return self.username #사용자 정보로 표시

    class Meta:  
        db_table = 'fastcampus_fcuser' # DB이름
        verbose_name = '장고사이트 사용자' # Class이름 웹상에서 보여줄때 (Fcuser -> 장고사이트 사용자)
        verbose_name_plural = '장고사이트 사용자' # 뒤에 s 붙는거 없애준다