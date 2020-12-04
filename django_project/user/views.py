from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import Dj_User

# Create your views here.

def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})

class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):        
        djuser = Dj_User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        djuser.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = '/' # 성공시 이동할곳

    def form_valid(self, form): # form에서 값을 제대로 받았을경우(로그인 성공한 경우)
        self.request.session['user'] = form.data.get('email')
        
        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    
    return redirect('/')