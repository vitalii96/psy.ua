from blog.models import Post
from .models import Psychologist


class DataMixin:
    def get_main_information(self, **kwargs):
        last_posts = Post.objects.all().order_by('-created_at')[:3]
        psychologist = Psychologist.objects.get(pk=1)

        context = {
            'last_posts': last_posts,
            'psychologist': psychologist,
        }
        return context
