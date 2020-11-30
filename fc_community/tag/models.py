from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    resistered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')
    
    def __str__(self): #Fcuser를 웹상에서 표시하는 함수
        return self.name #사용자 정보로 표시

    class Meta:  
        db_table = 'fastcampus_tag' # DB이름
        verbose_name = '장고사이트 태그' # Class이름 웹상에서 보여줄때 (Fcuser -> 장고사이트 사용자)
        verbose_name_plural = '장고사이트 태그' # 뒤에 s 붙는거 없애준다