from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView
from .utils import *
from .models import *
from menu import menu

menu = menu

class ShowTopics(ListView):
    model = Topic
    template_name = 'blog/topics.html'
    context_object_name = 'topics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'Блог'  # Замініть "Ваш заголовок" на потрібний вам заголовок
        context['title'] = title
        return context

class PostList(BlogMixin,ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = ''  # Замініть "Ваш заголовок" на потрібний вам заголовок
        context['title'] = title
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
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic_slug = self.kwargs['topic_slug']
        topic = self.get_topic_title(topic_slug)  # Отримати назву теми
        title = 'БЛОГ'
        c_def = self.get_posts_context(topic_selected=topic_slug)
        context['topic'] = topic
        context['title'] = title
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Post.objects.filter(topic__slug=self.kwargs['topic_slug'], is_published=True).select_related('topic', 'author')

    def get_topic_title(self, topic_slug):
        try:
            topic = Topic.objects.get(slug=topic_slug)
            return topic.title
        except Topic.DoesNotExist:
            return None  # Обробка ситуації, коли тему не знайдено

