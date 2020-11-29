from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.


# pk - 1번째글, 2번째글 ....
def board_detail(request, pk): 
    board = Board.objects.get(pk=pk)
    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if request.method =='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()
    
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    # Board에서 모든 요소를 가져오고 id를 최신 순으로 정렬한다
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})