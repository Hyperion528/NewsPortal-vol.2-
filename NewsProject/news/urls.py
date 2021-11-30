from django.urls import path
from .views import PostsList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView


 
urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_add'), 
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]

