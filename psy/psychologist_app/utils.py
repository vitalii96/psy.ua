from blog.models import Post
from .models import Psychologist


class DataMixin:
    def get_main_information(self, **kwargs):
        last_posts = Post.objects.all().order_by('-created_at')[:3]
        psychologist_contact = Psychologist.objects.filter(pk=1).values('contact_numbers', 'email').first()
        psychologist_phone_numbers = psychologist_contact['contact_numbers']
        psychologist_email = psychologist_contact['email']
        context = {
            'last_posts': last_posts,
            'psychologist_phone_numbers': psychologist_phone_numbers,
            'psychologist_email': psychologist_email,
        }
        return context
