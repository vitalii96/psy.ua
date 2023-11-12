from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views import View
from django.contrib.auth import logout
from telegram_bot_app.bot import SendInformationForm
from .models import Psychologist, ContentItems, Diploma, Certificate
from blog.models import Post
from psychologist_app.forms import HelpForm
from .utils import DataMixin


class Base(DataMixin, View):
    template_name = 'psychologist_app/base.html'

    def get_context_data(self, request):
        context = self.get_main_information()
        context['user'] = request.user
        return render(request, self.template_name, context)


class Index(DataMixin, View):
    template_name = 'psychologist_app/index.html'

    def get(self, request):
        context = self.get_main_information()
        content_main = ContentItems.objects.filter(sign__title='Основна')
        methodics = ContentItems.objects.filter(sign__title='Методика')
        questions = ContentItems.objects.filter(sign__title='Запит')
        psychologist = Psychologist.objects.get(pk=1)
        form = HelpForm()

        context['content'] = content_main
        context['methodics'] = methodics
        context['questions'] = questions
        context['form'] = form
        context['psychologist'] = psychologist
        context['title'] = 'Головна сторінка'

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


class Education(DataMixin, View):
    template_name = 'psychologist_app/education.html'

    def get(self, request):
        context = self.get_main_information()
        diplomas = Diploma.objects.all()
        certificates = Certificate.objects.all()
        context['diplomas'] = diplomas
        context['certificates'] = certificates
        context['title'] = 'Моя освіта'
        return render(request, self.template_name, context=context)

class About (DataMixin,View):
    template_name = 'psychologist_app/about.html'
    def get (self, request):
        psychologist = Psychologist.objects.get(pk=1)
        context = self.get_main_information()
        context['psychologist'] = psychologist
        context['title'] = 'Про мене'

        return render(request,self.template_name,context)


class ContactInformation (DataMixin,View):
    template_name = 'psychologist_app/contact.html'
    def get(self,request):
        psychologist = Psychologist.objects.get(pk=1)
        context = self.get_main_information()
        form = HelpForm()
        context['psychologist'] = psychologist
        context['form'] = form
        context['title'] = 'Контактна інформація'
        return render(request, self.template_name, context)
