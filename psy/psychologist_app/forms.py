from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

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


class HelpForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Номер телефону',}), label='Номер телефону')
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ваще ім'я"}),  label="Ім'я")
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Опис проблеми'}), required=True, max_length=255, label='Опис проблеми')
    telegram = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telegram'}), required=False, label='Telegram')
    captcha = CaptchaField(label='Капча')
