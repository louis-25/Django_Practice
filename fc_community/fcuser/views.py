from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password # 암호화
from .models import Fcuser # DB정보를 가져온다
from .forms import LoginForm

# Create your views here.

def home(request):      
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'): # user 세션 정보가 있으면
        del(request.session['user']) # user 세션 삭제
    
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): # 로그인 form을 확인해서 값이 잘 들어있으면
            # session
            request.session['user'] = form.user_id

            return redirect('/')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form':form})    
                

# url에 연결하면 요청정보가 request변수를 통해 들어온다
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)


        # 예외처리!
        res_data = {}
        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            # DB에 모델로 저장
            fcuser = Fcuser(
                username = username, # Fcuser의 username에 POST방식으로 전달받은 username을 넣어줌
                password = make_password(password),
                useremail = useremail
            )        

            fcuser.save() # 저장!

        # 반환하고싶은 html파일 (파일의 경로는 기본적으로 templates로 지정돼있다)
        # res_data가 register.html에 전달된다
        return render(request, 'register.html', res_data) 
    