from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    # path('posts/',cache_page(60)( PostList.as_view()), name='posts'),
    path('posts/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('topic/<slug:topic_slug>/', PostsTopics.as_view(), name='topic'),
    path('topic/', ShowTopics.as_view(), name='topics')
]