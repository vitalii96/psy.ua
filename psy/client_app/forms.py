from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.forms import ModelForm


class SessionRecordForm(ModelForm):
    class Meta:
        model = SessionRecord
        fields = ('session_date',)
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
            'session_time': forms.TimeInput(attrs={'type': 'time', 'step': '60'})
        }


class ClientCreateForm(ModelForm):
    class Meta:
        model = Client
        fields = ('contact_number', 'issue_description')


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'name': 'demo-name',
        'id': 'demo-name',
        'value': '',
        'placeholder': "Ім'я"

    }))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'demo-name',
            'id': 'demo-name',
            'value': '',
            'placeholder': "Пароль"
    }))
class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Користувач з таким ім'ям вже існує")
        return username

class UserProfileForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }