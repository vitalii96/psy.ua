from django.db.models import Count
from django.core.cache import cache
from .models import Topic, Post
menu = [
    {'title': 'Контакти', 'url_name': 'contact'},
    {'title': 'Про мене', 'url_name': 'about'},
    {'title': 'Відгуки', 'url_name': 'reviews'},
    {'title': 'Блог', 'url_name': 'posts'},
]


class BlogMixin:
    paginate_by = 3
    def get_posts_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        # Включення кешування вибірки
        # topics = cache.get('topics')
        # if not topics:
        #     topics = Topic.objects.annotate(Count('post')).filter(post__is_published=True)
        #     cache.set('topics', topics,60)
        topics = Topic.objects.annotate(Count('post')).filter(post__is_published=True)
        context['topics'] = topics
        if 'topic_selected' not in context:
            context['topic_selected'] = 0
        return context
