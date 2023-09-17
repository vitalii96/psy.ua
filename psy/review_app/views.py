from django.shortcuts import render
from .models import Review
from django.views.generic import CreateView, ListView
from review_app.forms import AddReviewForm
from menu import menu
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse

class AddReview(LoginRequiredMixin, CreateView):
    form_class = AddReviewForm
    template_name = 'review_app/add_review.html'


    def form_valid(self, form):
        review = form.save(commit=False)
        # Присвоюємо авторизованого користувача як автора відгуку
        review.client = self.request.user.client
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path

def add_review(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if request.user.is_authenticated:
            client = request.user.client
            review = Review.objects.create(client=client, content=content)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Ви не авторизовані'})

def reviews(request):
    reviews = Review.objects.all()
    context = {
        'menu': menu,
        'reviews': reviews,
    }

    return render(request, 'review_app/review_list.html', context=context)
