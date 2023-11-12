from django.contrib.auth.models import User
from django.forms import PasswordInput
# from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import *


class StartForm(forms.ModelForm):
    word = forms.CharField()

    class Meta:
        model = File
        fields = ['file']


class WordForm(forms.Form):
    word = forms.CharField()
