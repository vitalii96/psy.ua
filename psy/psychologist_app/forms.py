from django import forms
from captcha.fields import CaptchaField

class HelpForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Номер телефону',}), label='Номер телефону')
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ваще ім'я"}),  label="Ім'я")
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Опис проблеми'}), required=True, max_length=255, label='Опис проблеми')
    telegram = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telegram'}), required=False, label='Telegram')
    captcha = CaptchaField(label='Капча')
