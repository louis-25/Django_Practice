from django.shortcuts import redirect
from .models import Dj_User

def login_required(function):
    def wrap(request, *args, **kwargs): # 인자값은 통일해줘야한다
        user = request.session.get('user')
        if user is None or not user: # 로그인 안된상태이면 로그인페이지로
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap

def admin_required(function):
    def wrap(request, *args, **kwargs): # 인자값은 통일해줘야한다
        user = request.session.get('user')
        if user is None or not user: # 로그인 안된상태이면 로그인페이지로
            return redirect('/login')        

        user = Dj_User.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap