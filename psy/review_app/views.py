from django.shortcuts import render
from .models import Review
from client_app.models import Client
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

        # Перевірка, чи користувач є клієнтом
        if hasattr(self.request.user, 'client'):
            review.client = self.request.user.client
            review.save()
            return super().form_valid(form)
        else:
            return JsonResponse({'success': False, 'error': 'Ви не авторизовані або не є клієнтом'})

    def get_success_url(self):
        return self.request.path


def add_review(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if request.user.is_authenticated and hasattr(request.user, 'client'):
            client = request.user.client
            review = Review.objects.create(client=client, content=content)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Ви не авторизовані або не єте клієнтом'})


def reviews(request):
    reviews = Review.objects.all()

    # Перевірка, чи користувач є клієнтом
    client = request.user.client if request.user.is_authenticated and hasattr(request.user, 'client') else None

    context = {
        'menu': menu,
        'reviews': reviews,
        'client': client,
    }

    return render(request, 'review_app/review_list.html', context=context)
