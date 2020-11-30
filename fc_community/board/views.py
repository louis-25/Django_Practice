from django.shortcuts import render, redirect
from django.core.paginator import Paginator # Paginator는 page에 대한 정보를 담고있다
from django.http import Http404
from fcuser.models import Fcuser
from tag.models import Tag
from .models import Board
from .forms import BoardForm
# Create your views here.


# pk - 1번째글, 2번째글 ....
def board_detail(request, pk): 
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist: # 예외처리
        raise Http404('게시글을 찾을 수 없습니다') # django에서 제공하는 예외처리

    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if not request.session.get('user'): # 세션에 user가 없으면 (로그인 안된경우)
        return redirect('/fcuser/login/') # login 페이지로 이동

    if request.method =='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            
            for tag in tags:
                if not tag:
                    continue

                # name=tag조건이 일치하면 가져오고 없으면 생성해서 가져온다
                # _tag:객체를 반환 / created:생성이됐는지
                # _tag, created = Tag.objects.get_or_create(name=tag) 
                _tag, _ = Tag.objects.get_or_create(name=tag) # _ 는 두번째 객체를 받지 않겠다는 뜻
                board.tags.add(_tag)
            

            return redirect('/board/list/')
    else:
        form = BoardForm()
    
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    # Board에서 모든 요소를 가져오고 id를 최신 순으로 정렬한다
    all_boards = Board.objects.all().order_by('-id')
    page = request.GET.get('p', 1)
    paginator = Paginator(all_boards, 2) # 한 페이지당 몇개씩 보여줄지?

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})