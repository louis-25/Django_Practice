from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.board_detail), # detail/1 datail/2 ...
    path('list/', views.board_list),
    path('write/', views.board_write),
]

