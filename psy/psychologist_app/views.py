from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views import View
from django.contrib.auth import logout
from telegram_bot_app.bot import SendInformationForm
from .models import Psychologist, ContentItems
from blog.models import Post
from psychologist_app.forms import HelpForm
from .utils  import DataMixin


class Base(DataMixin, View):
    template_name = 'psychologist_app/base.html'
    def get_context_data(self, request):
        context = self.get_main_information()
        context['user'] = request.user
        return render(request, self.template_name, context)

class Index (DataMixin,View):
    template_name = 'psychologist_app/index.html'

    def get(self, request):
        content_main = ContentItems.objects.filter(sign__title='Основна')
        methodics = ContentItems.objects.filter(sign__title='Методика')
        questions = ContentItems.objects.filter(sign__title='Запит')
        form = HelpForm()

        context = {
            'content': content_main,
            'methodics': methodics,
            'questions': questions,
            'form': form,
            'psychologist': self.get_main_information()['psychologist'],
            'title': 'Головна сторінка',
            'last_posts': self.get_main_information()['last_posts'],
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = HelpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            telegram = form.cleaned_data['telegram']
            phone_number = form.cleaned_data['phone_number']
            description = form.cleaned_data['description']
            SendInformationForm(name, phone_number, description, telegram)
            form = HelpForm()
            return redirect('home')


class Education (DataMixin, View):
    template_name = 'psychologist_app/education.html'

    def get(self, request):
        context = self.get_main_information()
        return render(request, self.template_name, context=context)
def education(request):
    context = {
        'psylogist': psychologist,
    }
    return render(request, 'psychologist_app/education.html', context=context)

def about(request):
    context = {
        'psylogist': psychologist,
    }
    return render(request, 'psychologist_app/about.html', context=context)


def contact(request):
    context = {
        'psylogist': psychologist,
    }
    return render(request, 'psychologist_app/contact.html', context=context)
