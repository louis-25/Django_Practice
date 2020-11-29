from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, # 사용자가 삭제됐을경우 게시글도 삭제되게함
                                verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')
    
    def __str__(self): #Fcuser를 웹상에서 표시하는 함수
        return self.title #사용자 정보로 표시

    class Meta:  
        db_table = 'fastcampus_board' # DB이름
        verbose_name = '장고사이트 사용자' # Class이름 웹상에서 보여줄때 (Fcuser -> 장고사이트 사용자)
        verbose_name_plural = '장고사이트 사용자' # 뒤에 s 붙는거 없애준다