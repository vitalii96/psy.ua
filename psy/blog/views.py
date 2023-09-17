from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView
from .utils import *
from .models import *
from menu import menu

menu = menu


class PostList(BlogMixin,ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_posts_context(title='Блог')
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('topic','author') # жадібнй запит


class ShowPost(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'


def pageNotFound(request, exeption):
    return HttpResponse(f'Сторінку не знайдено')


class PostsTopics(BlogMixin,ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic_slug = self.kwargs['topic_slug']
        c_def = self.get_posts_context(topic_selected=topic_slug)
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Post.objects.filter(topic__slug=self.kwargs['topic_slug'], is_published=True).select_related('topic', 'author')

