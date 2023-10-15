from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from menu import menu
from telegram_bot_app.bot import SendInformationForm
from .models import Psychologist, ContentItems
from blog.models import Post
from psychologist_app.forms import HelpForm

menu = menu


def base(request):
    psychologist = Psychologist.objects.get(pk=1)
    context = {
        'psychologist': psychologist,
        'menu': menu,
    }
    return render(request, template_name='psychologist_app/base.html', context=context)
# def test(request):
#     context = {
#         'menu': menu,
#     }
#     return render(request, template_name='psychologist_app/test.html', context=context)


def index(request):
    psychologist = Psychologist.objects.get(pk=1)
    content_main = ContentItems.objects.filter(sign__title='Основна')
    methodics = ContentItems.objects.filter(sign__title='Методика')
    questions  = ContentItems.objects.filter(sign__title='Запит')
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            telegram = form.cleaned_data['telegram']
            phone_number = form.cleaned_data['phone_number']
            description = form.cleaned_data['description']
            SendInformationForm(name, phone_number, description, telegram)
            form = HelpForm()
            return redirect('home')

    else:
        form = HelpForm()


    context = {
        'content': content_main,
        'methodics': methodics,
        'questions': questions,
        'form': form,
        'psychologist': psychologist,
        'title': 'Головна сторінка',
    }
    return render(request, 'psychologist_app/index.html', context=context)


def about(request):
    psylogist = Psychologist.objects.get(pk=1)
    context = {
        'menu': menu,
        'psylogist': psylogist,
    }
    return render(request, 'psychologist_app/about.html', context=context)


def contact(request):
    psylogist = Psychologist.objects.get(pk=1)
    context = {
        'menu': menu,
        'psylogist': psylogist,
    }
    return render(request, 'psychologist_app/contact.html', context=context)
