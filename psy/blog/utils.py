from django.db.models import Count
from django.core.cache import cache
from .models import Topic, Post


class BlogMixin:
    paginate_by = 5
    def get_posts_context(self, **kwargs):
        context = kwargs
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
