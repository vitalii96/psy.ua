from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from menu import menu
from psychologist_app.forms import RegisterUserForm
from client_app.forms import *
from client_app.models import Client, SessionRecord
from django.utils import timezone
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('/')


def sign_in(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'client_app/sign_up.html', {'form': form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('home')
            else:
                form.add_error('password', "Невірне ім'я користувача, або пароль")


        # form is not valid or user is not authenticated
        return render(request, 'client_app/sign_up.html', {'form': form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'client_app/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Перевірка, чи користувач з таким іменем вже існує
        username = form.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'Користувач з таким іменем вже існує.')
            return self.form_invalid(form)

        # Виклик `form.save(commit=False)` створює об'єкт користувача, але не зберігає його в базу даних
        user = form.save(commit=False)

        # Встановлюємо пароль для користувача
        password = form.cleaned_data['password1']
        user.set_password(password)

        # Зберігаємо користувача в базу даних
        user.save()

        # Автоматичний вхід нового користувача
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return super().form_valid(form)


@method_decorator(login_required(login_url='register'), name='dispatch')
class SessionsList(ListView, LoginRequiredMixin):
    model = SessionRecord
    template_name = 'client_app/client_session.html'
    context_object_name = 'sessions'
    login_url = 'register'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self, ):
        user = self.request.user
        try:
            client = Client.objects.get(user=user)
        except Client.DoesNotExist:
            return SessionRecord.objects.none()
        return SessionRecord.objects.filter(client=client)

    def post(self, request, *args, **kwargs):
        # Отримати ідентифікатор сесії з POST-запиту
        session_id = request.POST.get('session_id')

        # Перевірити, чи існує сесія з таким ідентифікатором для поточного клієнта
        session = get_object_or_404(SessionRecord, pk=session_id, client=request.user.client)

        # Перевірити, чи статус сесії є 'confirmed' перед тим, як дозволити її скасування
        if session.status == 'confirmed' or session.status == 'pending_confirmation':
            session.status = 'canceled'
            session.save()

        # Перенаправити знову до списку сесій після скасування
        return redirect(reverse_lazy('sessions'))


@method_decorator(login_required(login_url='register'), name='dispatch')
class SessionRecordView(View):
    template_name = 'client_app/session_record.html'  # Вкажіть ім'я вашого шаблону

    # Додаємо декоратор для перевірки авторизації користувача
    def get(self, request):
        user = request.user
        try:
            client = Client.objects.get(user=user)
            form = SessionRecordForm(initial={'client': client})
            client_form = None
        except Client.DoesNotExist:
            client = None
            form = SessionRecordForm()
            client_form = ClientCreateForm()

        return render(request, self.template_name, {'form': form, 'client': client, 'client_form': client_form})

    def post(self, request):
        user = request.user
        try:
            client = Client.objects.get(user=user)
            form = SessionRecordForm(request.POST)
        except Client.DoesNotExist:
            client = None
            form = SessionRecordForm(request.POST)
            client_form = ClientCreateForm(request.POST)

            if client_form.is_valid():
                new_client = client_form.save(commit=False)
                new_client.user = user
                new_client.first_name = user.first_name
                new_client.last_name = user.last_name
                new_client.save()
                client = new_client

        if form.is_valid():
            session_record = form.save(commit=False)
            session_record.client = client
            session_record.save()
            return redirect('sessions')  # Вкажіть ім'я URL-шляху, на який потрібно перенаправити

        return render(request, self.template_name, {'form': form, 'client': client, 'client_form': client_form})


@method_decorator(login_required(login_url='register'), name='dispatch')
class ProfileView(View):
    template_name = 'client_app/profile.html'

    def get(self, request):
        return render(request, self.template_name)

@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправити користувача на сторінку профілю після збереження
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'client_app/edit_profile.html', {'form': form})