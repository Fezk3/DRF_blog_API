from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('create', PostCreate.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name="post_detail"),
    path('posts_for_author', ListPostsForAuthor.as_view(), name='posts_for_author'),
]
