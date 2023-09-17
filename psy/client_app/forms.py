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


class SignUpForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })

class UserProfileForm(forms.ModelForm):
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