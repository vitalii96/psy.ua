from django import forms
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)

